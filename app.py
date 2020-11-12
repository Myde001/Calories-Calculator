#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 21:27:38 2020

@author: olumideakinola
"""

from flask import Flask, request, render_template
from Calories import Calories

app = Flask(__name__)

port = 0
clarifai_key = 1
wolframalpha_key =2
config ={ port:8000,clarifai_key:"64f97bc1c2e34da9aeaf6103fea866d4",wolframalpha_key:"GPEART-TX26A29R4A" }

@app.route('/')
def myForm():
    return render_template('my-form.html')

@app.route('/join', methods=['GET','POST'])
def myFormPost():
    image_url = request.args.get('text')
    
    call_calories = Calories(config[clarifai_key],config[wolframalpha_key])
    calories_value = call_calories.getCalories(image_url)
    return render_template("my-form.html",image_url = image_url,calories_value=calories_value)
    
    

if __name__ =='__main__':
    
    app.run(debug = True, port = config[port])
