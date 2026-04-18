import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np  
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app=application

#imporrt ridge regression model
ridge_model = pickle.load(open('models/ridge.pkl', 'rb'))
standard_scaler = pickle.load(open('models/scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        Temperature = float(request.form['Temperature'])
        RH = float(request.form['RH'])
        Ws = float(request.form['Ws'])
        Rain = float(request.form['Rain'])
        FFMC = float(request.form['FFMC'])
        DMC = float(request.form['DMC'])
        ISI = float(request.form['ISI'])
        Classes = float(request.form['Classes'])
        Region = request.form['Region']

        input_data = np.array([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])
        input_data_scaled = standard_scaler.transform(input_data)
        prediction = ridge_model.predict(input_data_scaled)

        return render_template('home.html', result=prediction[0])

    else:
        return render_template('home.html')
    
    


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0', port=5000)

