from flask import Flask, render_template, request
import pickle 
import numpy as np
import pandas as pd
import json

app = Flask(__name__)

model = pickle.load(open("beng_price.pkl", 'rb'))



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    values = [x for x in request.form.values()]
    
    user_input = pd.DataFrame({
    'area_type': [f'{values[0]}'],
    'availability': [f'{values[1]}'],
    'location': [f'{values[2]}'],
    'size': [values[3]],
    'total_sqft': [values[4]],
    'bath': [values[5]],
    'balcony': [values[6]]
    })
    
    
    
    prediction = model.predict(user_input)
    
    return render_template("index.html", prediction_text=f"The estimated price based on chosen data is {round(prediction[0] * 100000 * 0.0115, 1)} usdt")

if __name__ == '__main__':
    app.run(debug=True)