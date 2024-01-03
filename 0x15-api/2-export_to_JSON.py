#!/usr/bin/python3
"""Dumps employee data into a json file"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    id = argv[1]

    user = requests.get(url + f"users/{id}").json()
    todos = requests.get(url + f"todos", params={"userId": id}).json()

    r = {id: [{"task": item['title'],
               "completed": item['completed'],
               "username": user['username']} for item in todos]}

    file = f"{id}.json"
    with open(file, "w") as f:
        json.dump(r, f)
