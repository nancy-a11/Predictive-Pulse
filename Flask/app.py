from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load('model/random_forest_stage_model.pkl')

# Encoding mappings
gender_map = {'Male': 0, 'Female': 1}
history_map = {'Yes': 1, 'No': 0}
patient_map = {'No': 0, 'Yes': 1}
medication_map = {'No': 0, 'Yes': 1}
severity_map = {'Mild': 0, 'Moderate': 1, 'Severe': 2}
breath_map = {'No': 0, 'Yes': 1}
visual_map = {'No': 0, 'Yes': 1}
nose_map = {'No': 0, 'Yes': 1}
when_map = {'<1 Year': 0, '1 - 5 Years': 1, '>5 Years': 2}
diet_map = {'No': 0, 'Yes': 1}

# Reverse stage map
inv_stage_map = {
    0: 'NORMAL',
    1: 'ELEVATED',
    2: 'HYPERTENSION (Stage-1)',
    3: 'HYPERTENSION (Stage-2)',
    4: 'HYPERTENSIVE CRISIS'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/details')
def details():
    return render_template('details.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data and map using encoding
    gender = gender_map[request.form['Gender']]
    age = float(request.form['Age'])
    history = history_map[request.form['History']]
    patient = patient_map[request.form['Patient']]
    medication = medication_map[request.form['TakeMedication']]
    severity = severity_map[request.form['Severity']]
    breath = breath_map[request.form['BreathShortness']]
    visual = visual_map[request.form['VisualChanges']]
    nose = nose_map[request.form['NoseBleeding']]
    when = when_map[request.form['Whendiagnoused']]
    systolic = float(request.form['Systolic'])
    diastolic = float(request.form['Diastolic'])
    diet = diet_map[request.form['ControlledDiet']]

    # Prepare final input
    features = np.array([[gender, age, history, patient, medication,
                          severity, breath, visual, nose, when,
                          systolic, diastolic, diet]])

    # Predict
    prediction = model.predict(features)[0]
    stage = inv_stage_map[prediction]

    # Pass systolic, diastolic, and stage to the template
    return render_template('prediction.html',
                           systolic=systolic,
                           diastolic=diastolic,
                           stage=stage)


if __name__ == '__main__':
    app.run(debug=True)
