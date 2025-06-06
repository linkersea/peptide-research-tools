# Peptide Research Tools

A comprehensive suite of web applications and visualization tools for peptide research, featuring machine learning-powered property prediction and grafting time calculation.

## 🧬 Project Overview

This repository contains two independent web applications and visualization tools:

### 1. Peptide Grafting Time Calculator
Interactive web tool for calculating peptide grafting times based on target concentrations.

### 2. Peptide Property Predictor  
Machine learning-powered predictor for peptide properties including antimicrobial activity (AMP), alkaline phosphatase activity (ALP), and Laplace-Wenzel parameters.

### 3. Visualization Tools
Advanced visualization suite for research data analysis and publication-quality plots.

## 📁 Project Structure

```
peptide-research-tools/
├── peptide-grafting-calculator/     # Flask app for grafting time calculation
├── peptide-property-predictor/      # ML-powered property prediction
├── visualization-tools/             # Research visualization suite
└── docs/                           # Documentation and guides
```

## 🚀 Quick Start

### Option 1: Deploy Individual Applications

Each application can be deployed independently:

**Peptide Grafting Calculator:**
```bash
cd peptide-grafting-calculator
pip install -r requirements.txt
python app.py
```

**Peptide Property Predictor:**
```bash
cd peptide-property-predictor
pip install -r requirements.txt
python app.py
```

### Option 2: Cloud Deployment

Both applications are ready for deployment on:
- ✅ **Railway.app** (Recommended - Free tier available)
- ✅ **Heroku** 
- ✅ **Vercel** (with serverless functions)
- ✅ **PythonAnywhere**

## 🔬 Features

### Peptide Grafting Calculator
- Real-time grafting time calculations
- Interactive web interface
- Symbolic mathematics solving
- English/Chinese UI support

### Property Predictor
- Pre-trained ML models
- Multiple property predictions (AMP, ALP, LW)
- 12,000+ training dataset
- Publication-ready results

### Visualization Tools
- Correlation heatmaps
- Radar charts
- Pareto front analysis
- Publication-quality outputs

## 🎯 Use Cases

- **Academic Research**: Journal article supplementary tools
- **Drug Discovery**: Peptide property screening
- **Materials Science**: Surface modification planning
- **Education**: Interactive peptide chemistry learning

## 📊 Data Sources

- 12,000+ peptide sequences dataset
- Pre-trained scikit-learn models
- Pareto optimization results
- Experimental validation data

## 🔧 Technologies

- **Backend**: Flask, Python
- **ML**: Scikit-learn, Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn
- **Frontend**: HTML5, CSS3, JavaScript
- **Deployment**: Docker-ready, Cloud-native

## 📖 Documentation

See individual README files in each subdirectory:
- [Grafting Calculator Guide](peptide-grafting-calculator/README.md)
- [Property Predictor Guide](peptide-property-predictor/README.md)
- [Deployment Instructions](docs/DEPLOYMENT.md)

## 🤝 Contributing

This project is designed for academic research use. Feel free to fork and adapt for your research needs.

## 📄 License

MIT License - See LICENSE file for details.

## 🔗 Citation

If you use these tools in your research, please cite:
```
[Your Paper Citation Here]
```

## 🌐 Live Demos

- **Grafting Calculator**: [部署中 - Deploy on Railway.app]
- **Property Predictor**: [部署中 - Deploy on Railway.app]

> 🚀 **部署状态**: 代码已上传至 [GitHub](https://github.com/linkersea/peptide-research-tools)，请按照部署指南在Railway.app上创建两个独立应用

---

*Built for the scientific community to advance peptide research* 🧪
