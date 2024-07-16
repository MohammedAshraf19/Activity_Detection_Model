# Human Activity Recognition (HAR) System - Machine Learning Model

This repository contains the Machine Learning model component of the Human Activity Recognition (HAR) System. The model is built using XGBoost and is designed to classify various human activities and detect falls.

## Table of Contents
- [Introduction](#What_is_HAR_SYSTEM)
- [Features](#features)
- [Usage](#usage)
- [Feature Engineering](#feature-engineering)
- [License](#Analysis)

## What is HAR SYSTEM
The Human Activity Recognition System is an advanced solution designed to monitor and classify human activities using data from accelerometer and gyroscope sensors. This system is particularly useful for elderly care, providing real-time activity recognition and fall detection to ensure the safety and well-being of individuals. The system includes a mobile application developed with Flutter, a machine learning model using XGBoost, and a backend built with Node.js.

## Features
- High accuracy activity classification using XGBoost
- Fall detection mechanism
- Preprocessing scripts for sensor data
- Model training and evaluation scripts

To use this application, follow these steps:

1. **Clone the Repository:**
2. **Install Dependencies**
3. **Run app.py**

## Feature Engineering

To improve the performance of our Human Activity Recognition (HAR) model, we perform extensive feature engineering on the accelerometer and gyroscope data. Here is an overview of the feature extraction process:

1. **Raw Data Processing**:
    - **Accelerometer Data (X, Y, Z)**
    - **Gyroscope Data (X, Y, Z)**

2. **Magnitude Calculation**:
    - **Accelerometer Magnitude**: \( \sqrt{X_{acc}^2 + Y_{acc}^2 + Z_{acc}^2} \)
    - **Gyroscope Magnitude**: \( \sqrt{X_{gyro}^2 + Y_{gyro}^2 + Z_{gyro}^2} \)

3. **Statistical Features**:
    - **Mean**: Average value of the signal.
    - **Standard Deviation**: Measure of the amount of variation in the signal.
    - **Variance**: Measure of the dispersion of the signal values.
    - **Maximum**: Highest value in the signal.
    - **Minimum**: Lowest value in the signal.
    - **Range**: Difference between the maximum and minimum values.
    - **Median**: Middle value of the signal when ordered.
    - **Interquartile Range (IQR)**: Measure of statistical dispersion.
    - **Skewness**: Measure of the asymmetry of the signal.
    - **Kurtosis**: Measure of the "tailedness" of the signal.

4. **Frequency Domain Features**:
    - **Fast Fourier Transform (FFT)**: Transform signal to frequency domain.
    - **Power Spectral Density (PSD)**: Measure of signal's power content.
    - **Frequency Domain Entropy**: Measure of signal complexity in frequency domain.

5. **Time Domain Features**:
    - **Root Mean Square (RMS)**: Measure of signal magnitude.
    - **Zero Crossing Rate (ZCR)**: Rate at which signal changes sign.
    - **Autocorrelation**: Measure of similarity between signal and a lagged version of itself.

6. **Additional Features**:
    - **Signal Magnitude Area (SMA)**: Sum of the absolute values of the signal.
    - **Tilt Angle**: Angle of the device based on accelerometer data.
    - **Jerk Signals**: Rate of change of acceleration.
    - **Correlation between Axes**: Correlation coefficient between different axes (X, Y, Z).

These features are crucial for capturing the underlying patterns in the sensor data, enabling our XGBoost model to accurately classify different activities and detect falls.

## Analysis
![Screenshot from 2024-07-16 14-50-48](https://github.com/user-attachments/assets/8b70dacd-d093-44f0-bfcf-1c938f0b48b6)
![Screenshot from 2024-07-16 14-51-13](https://github.com/user-attachments/assets/0c5ba135-4804-48a4-aa60-3bff6150c8cb)

