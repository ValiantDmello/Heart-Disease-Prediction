# Heart Disease Prediction

## Overview

This project aims to predict heart disease using machine learning techniques on the Heart Disease UCI dataset through various algorithms such as Logistic Regression, Random Forest, K-Nearest Neighbours (KNN), Support Vector Machine (SVM - Linear), SVM (Kernel RBF), and Decision Tree Classifier. The KNN model has been identified as the best-performing model with an accuracy of 88%.

## Repository Contents

* heart-disease.ipynb: Jupyter Notebook containing the code for data exploration, model training, and evaluation.
* heart.csv: Dataset used for training and testing the models.
* app/: Flask web application folder containing code for the user interface to make predictions using the trained KNN model.

## Running Flask App

1. Clone the Repository: <br>
```git clone https://github.com/your-username/heart-disease-prediction.git```

2. Navigate to app directory <br>
```cd heart-disease-prediction``` <br>
```cd app```

4. Install Dependencies: <br>
```pip install -r requirements.txt``` <br>

5. Run the Flask App: <br>
```python app.py``` <br>

Visit http://localhost:5000 in your web browser to use the prediction interface.
