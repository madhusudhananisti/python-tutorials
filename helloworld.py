# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 19:37:21 2025

@author: Dell
"""

print("Hello World")

x = ("hi", "hello", "world", 123)

print (x)

y = ["hi", "hello", "world", 123]

y[2] = "borld"

print (y)

sentences = ["How do I learn AI",
            "How do I start learning AI",
            "hi",
            "AI"]

result = []

for sentence in sentences:
    if(len(sentence) > 5):
        result.append(sentence)
print (result)

result_comprehension = [sentence for sentence in sentences if(len(sentence) > 5)]

print (result_comprehension)

students = {
    "Alice" : {"age": 22, "course": "AI"},
    "Steven": {"age":24, "course": "CyberSecurity"}
}

#nested dictionaries
print (students["Steven"]["age"])

for key, value in students.items():
    print(key)
    print(value)
    
#dictionary_comprehension
filtered_dictionary = {key: value for key, value in students.items() if(value["course"] == "CyberSecurity")}
print (filtered_dictionary)

def add(a, b):
  c = a + b
  print(f"Sum of {a} and {b} is {c}")
  
def subtract(a, b):
  c = a - b
  print(f"Difference of {a} and {b} is {c}")
  
def multiply(a, b):
  c = a * b
  print(f"Product of {a} and {b} is {c}")
  
add(10, 20)

def calculate(a: int, b: int, operation):
    operation(a, b)

calculate(10, 20, multiply)

