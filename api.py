# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 13:52:16 2025

@author: Dell
"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
# Root endpoint

@app.get("/welcome")
def welcome():
    return {"message": "Welcome to my fastapi app"}


@app.get("/helloworld")
def helloworld():
    return {"message": "My hello world GET API"};
    

#Example GET API with a parameter
@app.get("/user")
def user():
    return {
        "name":"Madhu",
        "website": "www.linked.com"
    };

@app.get("/user/{user_id}")
def userWithId(user_id: int):
    if(user_id == 1):
        return {
            "name": "Madhu",
            "website": "www.linked.com"
            }
    else:
        return {
            "name": "john"+str(user_id),
            "website": "www.linked.com"
            }
        
class User(BaseModel):
    age: int
    name: str
    email: str
    
users = []

@app.post("/users")
def create_user(user: User):
    users.append(user.dict())
    return {"message": "User added successfully", "total_users": len(users)}
