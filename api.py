# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 13:52:16 2025

@author: Dell
"""
from fastapi import FastAPI

app = FastAPI()
# Root endpoint

@app.get("welcome")
def welcome():
    return {"message": "Welcome to my fastapi app"}


    

