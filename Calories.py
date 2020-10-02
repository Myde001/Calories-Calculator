#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 00:45:03 2020

@author: olumideakinola
"""

from clarifai.rest import ClarifaiApp, Image as ClImage
from pathlib import Path 

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

import wolframalpha



class Calories:
 
    
    def __init__(self,image):
        self.image = image
    
    def getFoodName(self):
        self.lst=[]
        app = ClarifaiApp(api_key='64f97bc1c2e34da9aeaf6103fea866d4')
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
        self.getFoodName()
        result = self.result
        app_id = "GPEART-TX26A29R4A"
        client = wolframalpha.Client(app_id)
        ques = "What is the total calories of "+ result +"?"
        res = client.query(ques)
        answer = next(res.results).text
        return result+" has "+answer
    
           
        


'''link = input("Enter the link to the picture: ")
food = calories(link)
print(food.getCalories())'''
        


