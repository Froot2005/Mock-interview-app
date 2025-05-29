# api/index.py
import sys
import os

# Add the parent directory of 'api' to the Python path
# This allows importing interview_app from the root of your project
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the Flask app instance from your main file
# Assuming your main Flask app is defined in interview_app.py at the root
from interview_app import app

# Vercel expects a variable named 'app' (or 'application' if configured)
# that is a callable object representing your web application (your Flask app instance).
# By importing 'app' from interview_app, we satisfy this requirement.

# No need for app.run() here, Vercel's serverless environment handles execution.