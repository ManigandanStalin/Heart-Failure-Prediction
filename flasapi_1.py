# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 17:30:12 2021

@author: Manigandan Stalin
"""


from flask import Flask, request
import numpy as np
import pickle
import pandas as pd
import flasgger
from flasgger import Swagger

app=Flask(__name__)
Swagger(app)

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict',methods=["Get"])
def predict_note_authentication():
    
    """Let's Predict the Heart Failure: 
    SAMPLE::  Age (Number)(Eg: 40); Sex (Male -1 or Female- 0)(Eg:1);
    ChestpainType (ASY-0,ATA-1,NAP-2,TS-3) (Eg:2);
    RestingBP (Decimal)(Eg:145.0); Cholestrol (Decimal)(Eg: 256.0); FastingBS (Either 0 or 1)(Eg:1);
    RestingECG (LVH-0,Normal-1,ST-2),MaxHR (Number)(Eg:150); 
    ExerciseAngina (Yes-1,No-0)(Eg:1); OldPeak (Decimal)(Eg:0.0);
    STSlope (Down-0,Flat-1,Up-2)(Eg:2)
    
    ---
    parameters:  
      - name: Age
        in: query
        type: number
        required: true
      - name: Sex
        in: query
        type: number
        required: true
      - name: ChestPainType
        in: query
        type: number
        required: true
      - name: RestingBP
        in: query
        type: number
        required: true
      - name: Cholesterol
        in: query
        type: number
        required: true
      - name: FastingBS
        in: query
        type: number
        required: true
      - name: RestingECG
        in: query
        type: number
        required: true
      - name: MaxHR
        in: query
        type: number
        required: true
      - name: ExerciseAngina
        in: query
        type: number
        required: true
      - name: Oldpeak
        in: query
        type: number
        required: true
      - name: ST_Slope
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    Age=request.args.get("Age")
    Sex=request.args.get("Sex")
    ChestPainType=request.args.get("ChestPainType")
    RestingBP=request.args.get("RestingBP")
    Cholesterol=request.args.get("Cholesterol")
    FastingBS=request.args.get("FastingBS")
    RestingECG=request.args.get("RestingECG")
    MaxHR=request.args.get("MaxHR")
    ExerciseAngina=request.args.get("ExerciseAngina")
    Oldpeak=request.args.get("Oldpeak")
    ST_Slope=request.args.get("ST_Slope")
    prediction=classifier.predict([[Age,Sex,ChestPainType,RestingBP,Cholesterol,FastingBS,RestingECG,MaxHR,ExerciseAngina,Oldpeak,ST_Slope]])
    print(prediction)
    return "Result for heart failure:: "+str(prediction)


if __name__=='__main__':
    app.run()