#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 21:27:38 2020

@author: olumideakinola
"""

from flask import Flask, jsonify, request, render_template
from Calories import getCalories

app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/join', methods=['GET','POST'])
def my_form_post():
    link = request.form['text']
    cal = getCalories(link)
    return jsonify(result=cal)
    

if __name__ =='__main__':
    app.run(debug = True)