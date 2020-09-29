#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 21:27:38 2020

@author: olumideakinola
"""

from flask import Flask, jsonify, request, render_template
from Calories import Calories

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
    app.run(debug = True, port =8000)