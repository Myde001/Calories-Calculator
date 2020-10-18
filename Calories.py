#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 00:45:03 2020

@author: olumideakinola
"""

from clarifai.rest import ClarifaiApp, Image as ClImage
import wolframalpha
import os


class Calories:
 
    def __init__(self,image, API_KEY,API_ID):
        self.image = image
        self.API_KEY = API_KEY
        self.API_ID = API_ID
    
    def getFoodName(self):
        self.lst=[]
        API_KEY = os.getenv(self.API_KEY)
        app = ClarifaiApp(api_key=API_KEY)
        model = app.models.get('food-items-v1.0')
        image = ClImage(url=self.image)
        response_data = model.predict([image])
        concepts = response_data['outputs'][0]["data"]['concepts']
        max1 =max([concept['value']for concept in concepts])
        for concept in concepts:
            if concept['value']==max1:
                self.result = concept['name']
            return self.result
    
    
    def getCalories(self):
        result = self.getFoodName()
        ID = os.getenv(self.API_ID)
        app_id = ID
        client = wolframalpha.Client(app_id)
        ques = "What is the total calories of " + result + "?"
        res = client.query(ques)
        answer = next(res.results).text
        return result + " has " + answer
    
           

        


