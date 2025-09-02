# URL Shortener Service

A simple, fast, and reliable URL shortening service built with Flask.

## Features

- 🚀 Lightning-fast URL shortening
- 🎯 Pronounceable short codes
- 📱 Mobile-responsive design
- 🔒 Secure and private
- 💯 100% free to use

## Local Development

### Prerequisites

- Python 3.9+
- pip

### Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd "Short URL"
```

2. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and go to `http://localhost:5000`

## Deployment

### Heroku

1. Install Heroku CLI and login
2. Create a new Heroku app:
```bash
heroku create your-app-name
```

3. Deploy:
```bash
git add .
git commit -m "Initial deployment"
git push heroku main
```

4. Open your app:
```bash
heroku open
```

### Railway

1. Connect your GitHub repository to Railway
2. Railway will automatically detect the Python app
3. Deploy with one click

### Render

1. Connect your GitHub repository to Render
2. Create a new Web Service
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `gunicorn wsgi:app`
5. Deploy

### Vercel

1. Install Vercel CLI: `npm i -g vercel`
2. Deploy: `vercel`

## Environment Variables

- `PORT`: Port number (automatically set by deployment platforms)
- `FLASK_ENV`: Set to `production` for production deployment

## API Endpoints

- `GET /`: Main application interface
- `POST /api/shorten`: Shorten a URL
- `GET /<code>`: Redirect to original URL
- `GET /api/qrcode/<code>`: Generate QR code for short URL
- `GET /health`: Health check endpoint

## Troubleshooting

### Common Issues

1. **App not starting**: Check if all dependencies are installed
2. **Port already in use**: Change the port in app.py or set PORT environment variable
3. **CORS errors**: The app includes CORS support, but check your deployment platform settings
4. **Static files not loading**: Ensure index.html is in the root directory

### Debug Mode

For local development, you can enable debug mode by changing:
```python
app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
```

## License

This project is open source and available under the MIT License.
