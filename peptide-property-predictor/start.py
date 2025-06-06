#!/usr/bin/env python3
"""
Railway.app startup script for Peptide Property Predictor
"""
import os
import sys

if __name__ == "__main__":
    # Try to import and run the Flask app
    try:
        from app import app
        port = int(os.environ.get('PORT', 5000))
        print(f"Starting Peptide Property Predictor on port {port}")
        app.run(host='0.0.0.0', port=port, debug=False)
    except Exception as e:
        print(f"Error starting application: {e}")
        sys.exit(1)
