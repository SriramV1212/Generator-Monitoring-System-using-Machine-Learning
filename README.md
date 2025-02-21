# 🔌 Predictive Maintenance System for Diesel Generator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/pandas-150458?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![MQTT](https://img.shields.io/badge/MQTT-3C5280?style=flat&logo=eclipse-mosquitto&logoColor=white)](https://mqtt.org/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![Random Forest](https://img.shields.io/badge/Random_Forest-38B000?style=flat)](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html)

A machine learning-based solution for predicting maintenance needs and monitoring diesel generator parameters in real-time.

## 📊 Project Overview

This project implements a predictive maintenance system for diesel generators using machine learning algorithms to analyze time series data. The system monitors critical parameters 
such as:

1. **Coolant Temperature**  
2. **Oil Pressure**  
3. **Vibration Levels**  
4. **Exhaust Gas Temperature**  
5. **Fuel Consumption Rate**  
6. **Battery Voltage**  
7. **Engine Speed (RPM)**  
8. **Load Current**  
9. **Frequency (Hz)**  
10. **Running Hours**

The machine learning model predicts potential issues like the ones listed above, before they cause failures, reducing downtime and maintenance costs.

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
1. Data collection from diesel generator sensors
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
seaborn
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

### Data Engineering & Big Data Integration
- **Real-time Streaming Architecture**:
  - Implement Apache Kafka for high-throughput, fault-tolerant data streaming
  - Build real-time analytics with Kafka Streams or Apache Flink

- **Workflow Orchestration**:
  - Migrate to Apache Airflow for robust pipeline scheduling and monitoring
  - Implement DAGs for complex maintenance prediction workflows

- **Big Data Processing**:
  - Scale to distributed computing with Apache Spark for handling fleet-wide generator data
  - Implement batch processing with Hadoop ecosystem for historical analysis

- **Data Warehousing & Storage**:
  - Implement Snowflake data warehouse for flexible scaling and analytics
  - Utilize AWS S3 for cost-effective long-term storage of sensor data

- **Cloud Infrastructure**:
  - Migrate to AWS cloud infrastructure (EC2, Lambda, SageMaker)
  - Implement containerization with Docker and Kubernetes for deployments

- **Advanced Analytics**:
  - Develop a data lake architecture for combining structured and unstructured maintenance data
  - Implement dbt (data build tool) for analytics engineering and transformation


## 📝 Project Information

- **Development Period**: August 2023 - May 2024
- **Institution**: SSN College of Engineering
- **Contributors**: [Sriram Vivek , Sethuram Gautham Rajakumar]


## 📫 Contact

Feel free to reach out if you have any questions or would like to collaborate!

- Email: sriram.vivek@stonybrook.edu
- LinkedIn: https://www.linkedin.com/in/sriram-vivek-58a673269/


---

*This project was developed as part of academic curriculum at SSN College of Engineering.*
