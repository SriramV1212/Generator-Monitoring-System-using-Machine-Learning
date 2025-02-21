# 🔌 Predictive Maintenance System for Diesel Generator

A machine learning-based solution for predicting maintenance needs and monitoring diesel generator parameters in real-time.

## 📊 Project Overview

This project implements a predictive maintenance system for diesel generators using machine learning algorithms to analyze time series data. The system monitors critical parameters and predicts potential issues before they cause failures, reducing downtime and maintenance costs.

### 🎯 Key Features
- Machine learning models for predictive analytics
- Real-time parameter monitoring via MQTT protocol
- Web-based dashboard for parameter visualization
- Comparative analysis of multiple ML algorithms

## 🧠 Machine Learning Models

The system evaluates multiple algorithms to find the optimal predictive model:
- Linear Regression
- Logistic Regression
- Decision Trees
- Random Forest Regression (achieved 90.56% accuracy)
- Support Vector Machines

## 🔧 Technical Implementation

### Files
- `training.py` - Code for training the machine learning models
- `predicting.py` - Implementation of prediction functionality
- `data.csv` - Historical training dataset
- `inputdata.csv` - Input data format for predictions
- `test.html` - Web dashboard for real-time monitoring

### Data Flow
1. Time series data collection from diesel generator sensors
2. Data preprocessing and feature engineering
3. Model training and evaluation
4. Real-time data transmission via MQTT
5. Parameter visualization on web dashboard

## 📈 Results

- **Best Performing Model**: Random Forest Regression
- **Accuracy**: 90.56%
- **Key Parameters Monitored**:
  - Voltage
  - Current
  - Fuel levels
  - Engine temperature
  - Operational hours

## 🚀 Getting Started

### Prerequisites
```
Python 3.7+
pandas
scikit-learn
paho-mqtt (for MQTT communication)
matplotlib (for visualization)
```

### Installation
1. Clone this repository
```bash
git clone https://github.com/yourusername/diesel-generator-predictive-maintenance.git
```

2. Install required packages
```bash
pip install -r requirements.txt
```

3. Run the training script
```bash
python training.py
```

4. Set up prediction system
```bash
python predicting.py
```

## 🔮 Future Work

- Integration with mobile alert systems
- Expanded parameter monitoring
- Edge computing implementation for remote generators
- Transfer learning for different generator models

## 📝 Project Information

- **Development Period**: August 2023 - May 2024
- **Institution**: SSN College of Engineering
- **Contributors**: [Your Name]

## 📊 Demo

![System Dashboard](https://via.placeholder.com/800x400?text=Dashboard+Screenshot)

## 📫 Contact

Feel free to reach out if you have any questions or would like to collaborate!

- [Your Email]
- [Your LinkedIn]
- [Your Portfolio]

---

*This project was developed as part of academic curriculum at SSN College of Engineering.*
