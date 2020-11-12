#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 00:45:03 2020

@author: olumideakinola
"""

from clarifai.rest import ClarifaiApp, Image as ClImage
import wolframalpha



class Calories:
 
    def __init__(self, api_key,api_id):
        
        self.api_key = api_key
        self.api_id = api_id
        self.app = ClarifaiApp(api_key=self.api_key)
        self.client = wolframalpha.Client(self.api_id)
    
    def getFoodName(self,image):
        self.lst=[]
        model = self.app.models.get('food-items-v1.0')
        image_val = ClImage(url=image)
        response_data = model.predict([image_val])
        concepts = response_data['outputs'][0]["data"]['concepts']
        max1 =max([concept['value']for concept in concepts])
        for concept in concepts:
            if concept['value']==max1:
                self.result = concept['name']
            return self.result
    
    
    def getCalories(self,image):
        result = self.getFoodName(image)
        ques = "What is the total calories of " + result + "?"
        res = self.client.query(ques)
        answer = next(res.results).text
        return "The food displayed is "+result + ", it has " + answer
    
           

        


