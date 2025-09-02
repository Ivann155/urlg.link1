from flask import Flask, request, jsonify, redirect, url_for, send_from_directory, send_file
from flask_cors import CORS
import random
import io
import qrcode
import os

app = Flask(__name__)
CORS(app)

# In-memory storage for short codes to URLs
url_map = {}

# Syllable components for generating pronounceable codes
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
vowels = ['a', 'e', 'i', 'o', 'u']

def generate_pronounceable_code(length=3):
    """Generate a short, pronounceable code using consonant-vowel patterns"""
    code = ''
    for i in range(length):
        if i % 2 == 0:  # Even positions get consonants
            code += random.choice(consonants)
        else:  # Odd positions get vowels
            code += random.choice(vowels)
    return code

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy', 'message': 'URL shortener service is running'})

@app.route('/api/shorten', methods=['POST'])
def shorten_url():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid JSON data'}), 400
            
        long_url = data.get('url')
        if not long_url:
            return jsonify({'error': 'No URL provided'}), 400
        
        # Basic URL validation
        if not long_url.startswith(('http://', 'https://')):
            return jsonify({'error': 'Invalid URL format. Must start with http:// or https://'}), 400
        
        # Generate a unique pronounceable code
        code = generate_pronounceable_code()
        
        # Ensure uniqueness by trying different codes if needed
        attempts = 0
        while code in url_map and attempts < 50:
            code = generate_pronounceable_code()
            attempts += 1
        
        # If still not unique after many attempts, add a number
        if code in url_map:
            base_code = code
            counter = 1
            while f"{base_code}{counter}" in url_map and counter < 10:
                counter += 1
            code = f"{base_code}{counter}"
        
        url_map[code] = long_url
        # Use request.host_url to get the correct base URL
        short_url = request.host_url.rstrip('/') + '/' + code
        return jsonify({'short_url': short_url})
        
    except Exception as e:
        print(f"Error shortening URL: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/<code>')
def redirect_to_long_url(code):
    long_url = url_map.get(code)
    if long_url:
        return redirect(long_url)
    return 'URL not found', 404

@app.route('/api/qrcode/<code>')
def get_qr_code(code):
    # Build the full short URL
    short_url = request.host_url + code
    # Generate QR code image
    img = qrcode.make(short_url)
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)
    return send_file(buf, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)
