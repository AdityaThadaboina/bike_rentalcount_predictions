from flask import Flask,render_template,request
import pickle
import numpy as np
from random import randint 
import xgboost as xgb;


app= Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods = ['POST'])

def predict():

    if request.method == 'POST':

        mon = request.form['mon']
        wd = request.form['wd']
        hol = request.form['hol']
        wekd = request.form['wekd']
        sea = request.form['sea']
        ws = request.form['ws']
        temp = request.form['temp']
        hum = request.form['hum']
        sp = request.form['sp']
    

        count = np.array([[int(sea),randint(0,1),int(mon),int(hol),int(wd),int(wekd),int(ws),float(temp)/41,float(hum)/100,float(sp)/67]])
        
        model = pickle.load(open('bsp.pkl','rb'))
        prediction = model.predict(count)

    return render_template('index.html', prediction = str(int(prediction[0])))

if __name__=='__main__':
    app.run()