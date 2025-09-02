#!/bin/bash

echo "🚀 Copying deployment files to your project..."

# Copy all deployment files to the parent directory (your main project)
cp wsgi.py ../
cp Procfile ../
cp runtime.txt ../
cp requirements.txt ../
cp app.py ../
cp README.md ../

echo "✅ All files copied successfully!"
echo ""
echo "Next steps:"
echo "1. Install new dependencies: pip install flask-cors gunicorn"
echo "2. Test locally: python app.py"
echo "3. Deploy to your platform of choice!"
echo ""
echo "Your URL shortener is now ready for deployment! 🎉"
