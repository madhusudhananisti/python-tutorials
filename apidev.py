# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 16:35:22 2025

@author: Dell
"""
import requests
import json

url = "https://api.restful-api.dev/objects/ff8081819782e69e019aafc939da56a9"

response = requests.get(url)

data = response.json()

print("Response json():")
print (data)

payload = {
  "name": "Apple MacBook Pro 32",
  "data": {
    "year": 2040,
    "price": 1849.99,
    "CPU model": "Intel Core i9",
    "Hard disk size": "1 TB"
  }
}

headers = {
        "Content-Type": "application/json"
    }

response = requests.post(url, headers=headers, data=json.dumps(payload))

if response.status_code == 200 or response.status_code == 201:
    print("Post successful")
    print("Response JSON:")
    print(response.json())
else:
    print(f"Request failed with status_code::{response.status_code}")
    print(response.text)        

