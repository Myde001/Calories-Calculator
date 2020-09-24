#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 21:27:38 2020

@author: olumideakinola
"""

from flask import Flask, jsonify, request

app = Flask(__name__)



@app.route('/', methods=['GET'])
def getURL():
    link = input("Enter the link to the picture: ")
    return link
app.run()