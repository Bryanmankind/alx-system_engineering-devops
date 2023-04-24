#!/usr/bin/python3
"""This code will return the to-do list of employees"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    name_ = requests.get(url + "users/{}".format(sys.argv[1])).json()
    toDo = requests.get(url + "toDo", params={"userId": sys.argv[1]}).json()

    finished_to_do = [f.get("title") for f in toDo if f.get("finished_to_do") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        name_.get("name"), len(finished_to_do), len(toDo)))
    [print("\f {}".format(b)) for b in finished_to_do]
