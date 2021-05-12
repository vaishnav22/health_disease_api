import requests
# from data_input import data_in
import json

URL = "http://127.0.0.1:5000/predict"
headers = {"Content-Type": "application/json"}
data = {"input": ['back_pain','weakness_in_limbs','neck_pain','dizziness','loss_of_balance']}

r = requests.post(URL,headers=headers,json=data)

print(r.json())