# Peptide Property Predictor

A machine learning-powered web application for predicting peptide properties including AMP (antimicrobial activity), ALP (alkaline phosphatase activity), and LW (Laplace-Wenzel parameters).

## Features
- Predict AMP, ALP, and LW properties from peptide sequences
- Multiple pre-trained machine learning models
- User-friendly web interface
- Real-time predictions

## Models
- `trained_AMP_model.pkl` - Antimicrobial activity prediction
- `trained_ALP_model.pkl` - Alkaline phosphatase activity prediction  
- `trained_lw_model.pkl` - Laplace-Wenzel parameter prediction
- `trained_model.pkl` - General peptide property model

## Usage
1. Enter a peptide sequence (amino acid codes)
2. Select the property to predict
3. Get instant ML-powered predictions

## Local Development
```bash
pip install -r requirements.txt
python app.py
```

## Deployment
Ready for deployment on cloud platforms with pre-trained models included.

## Technologies
- Flask (web framework)
- Scikit-learn (machine learning)
- Pandas & NumPy (data processing)
- Pre-trained ML models
