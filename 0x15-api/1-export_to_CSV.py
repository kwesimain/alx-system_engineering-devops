#!/usr/bin/python3
"""Exports data in the CSV format"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]

    user = requests.get(url + f"users/{user_id}").json()
    todos = requests.get(url + f"todos", params={"userId": user_id}).json()

    file = f"{user_id}.csv"
    with open(file, "w") as f:
        for item in todos:
            f.write(
                f'"{user_id}","{user["username"]}","{item["completed"]}",'
                f'"{item["title"]}"\n'
            )
