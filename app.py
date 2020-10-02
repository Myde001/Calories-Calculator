#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 21:27:38 2020

@author: olumideakinola
"""

from flask import Flask, jsonify, request, render_template
from Calories import Calories
import os
from pathlib import Path 

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)


@app.route('/')
def myForm():
    return render_template('my-form.html')

@app.route('/join', methods=['GET','POST'])
def myFormPost():
    image_filepath = request.form['text']
    call_calories = Calories(image_filepath)
    calories_value = call_calories.getCalories()
    return jsonify(result=calories_value)
    

if __name__ =='__main__':
    PRT = os.getenv("Port")
    app.run(debug = True, port =PRT)
