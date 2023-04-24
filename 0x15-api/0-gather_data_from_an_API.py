#!/usr/bin/python3
"""Returns to-do information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    userNm = requests.get(url + "users/{}".format(sys.argv[1])).json()
    toDo = requests.get(url + "toDo", params={"userId": sys.argv[1]}).json()

    finished = [d.get("title") for d in toDo if d.get("finished") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        userNm.get("name"), len(finished), len(toDo)))
    [print("\t {}".format(x)) for x in finished]
