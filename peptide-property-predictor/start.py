#!/usr/bin/env python3
"""
Railway.app startup script for Peptide Property Predictor with Python 3.12 compatibility
"""
import os
import sys

# Python 3.12 compatibility fixes
if sys.version_info >= (3, 12):
    # Set environment variables for distutils compatibility
    os.environ.setdefault('SETUPTOOLS_USE_DISTUTILS', 'stdlib')
    
    # Handle potential distutils import issues
    try:
        import distutils
    except ImportError:
        print("Warning: distutils not available, using setuptools fallback")

# Ensure the app directory is in Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

if __name__ == "__main__":
    # Try to import and run the Flask app
    try:
        from app import app
        port = int(os.environ.get('PORT', 5000))
        print(f"Starting Peptide Property Predictor on port {port}")
        print(f"Python version: {sys.version}")
        app.run(host='0.0.0.0', port=port, debug=False)
    except Exception as e:
        print(f"Error starting application: {e}")
        sys.exit(1)
