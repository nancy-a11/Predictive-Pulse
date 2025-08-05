#  Predictive Pulse – Blood Pressure Prediction Using AI & ML

A smart and user-friendly Blood Pressure Stage Prediction system that uses Machine Learning to analyze health parameters and predict hypertension stages. This application is built using Python, Flask for the backend, and Jupyter Notebook for model development and experimentation.

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
   - Dataset provided by the trainer
2. **Preprocessing**
   - Handling missing values, encoding categorical data
3. **EDA (Exploratory Data Analysis)**
   - Visualized using Seaborn and Matplotlib
4. **Model Building**
   - Algorithms: Random Forest, Logistic Regression, Naive Bayes, Decision Tree(classification models)
5. **Evaluation**
   - Metrics: Accuracy, Precision, Recall, F1-Score, Confusion Matrix
6. **Hyperparameter Tuning**
   - GridSearchCV used for Random Forest optimization
7. **Deployment**
   - Model served through Flask backend with an interactive UI

---

##  Project Structure
```
Predictive Pulse/
│
├── app.py # Flask backend application
├── templates/ # HTML Templates
│ ├── index.html # Home page
│ ├── header.html # Header component
│ ├── footer.html # Footer component
│ ├── prediction.html # Prediction result page
│ └── detail.html # Detailed insights page
│
├── static/ # Static files
│ └── hypertension.png # UI image (example)
│
├── model/
│ └── random_forest_stage_model.pkl # Serialized Random Forest model
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```
---

## 🛠 Tech Stack

- **Python 3.8+**
- **Flask**
- **Scikit-learn**
- **Pandas**
- **Matplotlib & Seaborn**
- **Jupyter Notebook**
- **HTML/Tailwind CSS**

---

##  Model Performance

-  **Random Forest** achieved the best results:
  - **Accuracy:** ~93%
  - **F1 Score:** 0.91
  - Hyperparameters tuned using GridSearchCV

---
## 🌍 Deployment & Hosting

The project is deployed using **[Render](https://render.com/)** – a cloud platform for hosting full-stack applications.

🔗 **Live Project Link**: [https://your-live-render-link.onrender.com](https://predictive-pulse-flask.onrender.com)  

Render makes deployment seamless with automatic builds from GitHub and a production-ready environment.

##  How to Run Locally

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

Made by:
- [@nancy-a11](https://github.com/nancy-a11)
- [@tiwarisristy](https://github.com/tiwarisristy)
- [@NITB1810](https://github.com/NITB1810)
- [@amitsavani-45](https://github.com/amitsavani-45)


## 📌 Acknowledgments

- **The SmartBridge Experimental Learning Program**


---
