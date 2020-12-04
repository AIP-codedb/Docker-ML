# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 23:56:40 2020

@author: amitkumar

This can be tested via postman
or
flasgger - pip install flasgger
"""

from flask import Flask,request
import pandas as pd
import pickle

#point from where the execution will start
app=Flask(__name__)

pickle_in=open('classifier.pkl','rb')
classifier=pickle.load(pickle_in)

# decorator for root path
@app.route('/')
def welcome():
    print(1)
    return "Welcome all gals"


'''
Get call using URL like something below
http://127.0.0.1:5000/predict?var=2&skew=3&curt=-1&entr=4
'''
@app.route('/predict')
def predict_note():
    var=request.args.get('var')
    skew=request.args.get('skew')
    curt=request.args.get('curt')
    entr=request.args.get('entr')
    
    pred = classifier.predict([[var,skew,curt,entr]])
    
    return "The predicted value is : "+ str(pred)

@app.route('/predict_file',methods=["POST"])
def bulk_predict():
    print(1)
    df_test = pd.read_csv(request.files.get("file"))
    print(2)
    pred = classifier.predict(df_test)
    
    return "The predicted value is : "+ str(list(pred))


if __name__=='__main__':
    app.run(host='0.0.0.0',port=8003)
