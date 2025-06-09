# setup.py compatibility layer for Python 3.12
# This file helps resolve distutils module issues during deployment

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup
    find_packages = lambda: []

import sys
import os

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Ensure setuptools uses stdlib distutils for Python 3.12 compatibility
if sys.version_info >= (3, 12):
    import os
    os.environ.setdefault('SETUPTOOLS_USE_DISTUTILS', 'stdlib')

if __name__ == "__main__":
    setup(
        name="peptide-property-predictor",
        version="1.0.0",
        description="Peptide Property Predictor with ML",
        packages=find_packages(),
        install_requires=[
            "Flask>=3.1.0",
            "numpy==1.26.4",
            "pandas>=2.0.0",
            "scikit-learn>=1.3.0",
            "setuptools>=70.0.0",
            "wheel>=0.43.0"
        ],
        python_requires=">=3.12"
    )
