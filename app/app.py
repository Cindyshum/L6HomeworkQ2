from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from joblib import load
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    request_type_str = request.method
    if request_type_str == 'GET':
        return render_template('index.html', href2='', href3='')
    else:
        myage = request.form['age']
        mygender = request.form['gender']
        myacademic = request.form['academic']
        model = load('app/music-recommender.joblib')
        np_arr = np.array([myage, mygender, myacademic])
        # np_arr = [myage, mygender, myacademic]
        predictions = model.predict([np_arr])  
        predictions_to_str = str(predictions)
        #return predictions_to_str
        return render_template('index.html', 
                               href2=
                               'The suitable music for you (age:'+str(myage)+
                               ' ,gender:'+str(mygender)+
                               # ' ,academic-qualification:' +str(myacademic)+
                               ' )is: ',
                               href3=predictions_to_str
                            )
