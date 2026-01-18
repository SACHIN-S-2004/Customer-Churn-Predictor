<div align="center">
  
# 📉 Customer Churn Predictor
🚀 **ML-Powered Customer Retention Intelligence**

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikit-learn)
![Flask](https://img.shields.io/badge/Flask-Web_App-green?style=for-the-badge&logo=flask)
![Bootstrap](https://img.shields.io/badge/Bootstrap-UI-purple?style=for-the-badge&logo=bootstrap)
![Chart.js](https://img.shields.io/badge/Chart.js-Visualization-orange?style=for-the-badge&logo=chartdotjs)

Identify whether the customers are likely to stay or churn using Machine Learning — instantly and accurately
</div>

------------------------------------------------------------------------

## 📌 Project Overview

The **Customer Churn Predictor** is an end-to-end **Machine Learning +
Web Application** designed to help businesses identify customers who are
likely to leave (churn).

Unlike basic classifiers, this project: 
- Predicts **Churn / No Churn**
- Shows **confidence percentage (%)**
- Visualizes prediction confidence using **interactive graphs**
- Uses a **production-ready ML pipeline**

------------------------------------------------------------------------

## ✨ Key Features

-   ✅ Churn / No Churn prediction
-   📊 Probability-based confidence score
-   📈 Interactive visualization (Chart.js)
-   🎨 Production-grade Bootstrap UI
-   🧠 End-to-end ML pipeline (preprocessing + model)
-   🔒 Safe handling of unseen categorical values

------------------------------------------------------------------------

## 🖼️ Sample Screenshots

<div align="center">

### 💻 Webpage - Responsive Design

![alt text](sampleScreenshots/Screenshot%202026-01-18%20122617.png)

### 📊 Prediction Results

![alt text](sampleScreenshots/Screenshot%202026-01-18%20124140.png)

![alt text](sampleScreenshots/Screenshot%202026-01-18%20124607.png)

*Real-time classification results*

</div>

------------------------------------------------------------------------

## 🧠 Machine Learning Workflow

### 🔹 Data Preprocessing

Handled **inside the pipeline**: - One-Hot Encoding for categorical features
- Numerical features passed directly
- `handle_unknown="ignore"` for robust inference

### 🔹 Features Used

-   Age
-   Gender
-   Tenure
-   Usage Frequency
-   Support Calls
-   Payment Delay
-   Subscription Type
-   Contract Length
-   Total Spend
-   Last Interaction

------------------------------------------------------------------------

## 🧪 Models Trained & Evaluated

During experimentation in the Jupyter Notebook (`.ipynb`), the following
**supervised classification models** were trained and evaluated:

### 1️⃣ Logistic Regression

-   Used as a **baseline model**
-   Fast and interpretable
-   Performs well on linearly separable data
-   Limited in capturing complex, non-linear relationships

### 2️⃣ Random Forest Classifier

-   Ensemble-based model using multiple decision trees
-   Handles non-linear patterns well
-   Robust to outliers and noise
-   Provides good performance but can be less stable for probability
    estimates

### 3️⃣ Gradient Boosting Classifier

-   Sequential ensemble model
-   Focuses on correcting previous model errors
-   Excellent performance on structured/tabular data
-   Produces reliable probability scores

------------------------------------------------------------------------

## 🏆 Model Selection

After comparing all trained models, **Gradient Boosting Classifier** was
selected as the final model.

### 🔍 Why Gradient Boosting?

| Criteria | Gradient Boosting | Random Forest | Logistic Regression |
|----------|-------------------|---------------|---------------------|
| Non-linear learning | ✅ Excellent | ✅ Good | ❌ Limited |
| Probability quality | ✅ High | ⚠️ Medium | ⚠️ Medium |
| Tabular data performance | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| Business reliability | ✅ Strong | ✅ Good | ⚠️ Basic |

### ✅ Final Choice

➡️ **Gradient Boosting Classifier with a Scikit-learn Pipeline**

This choice ensures: 
- Higher predictive accuracy
- More reliable confidence percentages
- Better generalization on real-world customer data

------------------------------------------------------------------------

## 🌐 Web Application Overview

### 🖥️ Frontend

-   Bootstrap-based dashboard UI
-   Dropdowns for categorical features
-   Responsive & clean layout
-   Doughnut chart for probability visualization

### ⚙️ Backend

-   Flask server
-   Loads trained ML pipeline (`.pkl`)
-   Uses `predict_proba()` for confidence scoring

### 📊 Output

-   **Churn 🚨 / No Churn ✅**
-   Confidence percentage (%)
-   Interactive visual graph

------------------------------------------------------------------------

## 🚀 How to Run the Project

### Clone the repository
``` bash
git clone https://github.com/your-username/Customer-Churn-Predictor.git
```

### Navigate to project directory
```bash
cd Customer-Churn-Predictor
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run the Flask app
```bash
python app.py
```

Open in browser:

    http://127.0.0.1:5000

------------------------------------------------------------------------

## 📊 Sample Output

    Prediction: No Churn ✅
    Stay Probability: 86%
    Churn Probability: 14%

------------------------------------------------------------------------

## 📌 Business Value

-   Identify high-risk customers early
-   Enable proactive retention strategies
-   Reduce customer churn
-   Support data-driven decision making

------------------------------------------------------------------------

## 👨‍💻 Author

**Sachin Suresh**
Machine Learning & Full-Stack Developer

⭐ *If you find this project useful, consider giving it a star!*
