#  Predictive Pulse – Blood Pressure Prediction Using AI & ML

A smart and user-friendly Blood Pressure Prediction system that uses Machine Learning to analyze health parameters and predict hypertension stages. This application is built using Python, Flask for the backend, and Jupyter Notebook for model development and experimentation.

---

##  Features

-  Flask-based web application with a clean HTML UI
-  ML models including Random Forest, Logistic Regression, and Naive Bayes
-  Real-time prediction of blood pressure category (e.g., Normal, Elevated, Hypertension)
-  Jupyter Notebook used for EDA, model building, and evaluation
-  Model serialization using `joblib`
-  Performance analysis with accuracy, F1-score, precision, and confusion matrix

---

##  Machine Learning Pipeline

1. **Data Collection**
   - Dataset used from [Kaggle - Blood Pressure Dataset](https://www.kaggle.com/)
2. **Preprocessing**
   - Handling missing values, encoding categorical data
3. **EDA (Exploratory Data Analysis)**
   - Visualized using Seaborn and Matplotlib
4. **Model Building**
   - Algorithms: Random Forest, Logistic Regression, Naive Bayes, Decision Tree, KNN
5. **Evaluation**
   - Metrics: Accuracy, Precision, Recall, F1-Score, Confusion Matrix
6. **Hyperparameter Tuning**
   - GridSearchCV used for Random Forest optimization
7. **Deployment**
   - Model served through Flask backend with an interactive UI

---

##  Project Structure
```
BloodPressurePredictor/
│
├── app.py                      # Flask backend
├── templates/
│   └── index.html              # Web UI
├── static/
│   └── style.css               # Optional CSS file
├── model/
│   └── bp_model.pkl            # Trained ML model (serialized)
├── notebooks/
│   └── blood_pressure_model.ipynb   # Jupyter Notebook with EDA and training
└── README.md
```
---

## 🛠 Tech Stack

- **Python 3.8+**
- **Flask**
- **Scikit-learn**
- **Pandas**
- **Matplotlib & Seaborn**
- **Jupyter Notebook**
- **HTML/CSS**

---

##  Model Performance

-  **Random Forest** achieved the best results:
  - **Accuracy:** ~93%
  - **F1 Score:** 0.91
  - Hyperparameters tuned using GridSearchCV

---

##  How to Run

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/BloodPressurePredictor.git
cd BloodPressurePredictor
```
2. **Create Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Run Flask App**
```bash
python app.py
```

5. **Open in Browser**
```
http://127.0.0.1:5000/
```

---

##  Contributors

Made with  by:
- [@nancy-a11](https://github.com/nancy-a11)
- [@tiwarisristy](https://github.com/tiwarisristy)
- [@NITB1810](https://github.com/NITB1810)
- [@amitsavani-45](https://github.com/amitsavani-45)


## 📌 Acknowledgments

- **SmartInternz Internship Program**


---
