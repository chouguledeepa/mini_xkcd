"""
The star WAR API lists 82 main characters in the star wars sanga.For The First task  we would like you to use
a random number generator  that picks a number between 1 - 82
the see random numbers you will be pulling 15 characters
from the API using python

"""

import requests
from utils.randomnum import random_numbers

start = 1
stop = 15

obj = random_numbers()
random_numbers = []

for i in range (start,stop+1):
    random_numbers.append(next(obj))

# class swapi:
#     def __init__(self):
#         home_url = "https://swapi.dev"
#         resources = ["planets","films",'people','spaceship']

    if __name__ == "__main__":
        print(__name__)
        print("current module getting executed")
        print("character name in film1",)

        home_url = "https://swapi.dev"
        relative_url = "/api/planets/1/" #magic string

        for num in random_numbers:
            absolute_url = home_url + relative_url .format(num)
            print(f"feaching details using {absolute_url}->\n")
            responce = requests.get(absolute_url)
            responce = responce.json()
            print(responce)
            print("######"*25)


        character_name = []
        for names in random_numbers:
            print(names)
            character_name.append(names)

