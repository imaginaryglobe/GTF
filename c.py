""" 

This script is used to check if all the countries in the reversed_countries.json file have a corresponding image in the images folder.

"""



import json

import os

with open("reversed_countries.json") as file:
    data = json.load(file)
    COUNTRY_LIST = [country.lower() for country in data]
    #print(COUNTRY_LIST[0])


directory = os.fsencode("images/")

IMG_NAME_LIST = []
 
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    IMG_NAME_LIST.append(filename[0:2])



print(len(IMG_NAME_LIST))
print(len(COUNTRY_LIST))

for country in COUNTRY_LIST:
    if country not in IMG_NAME_LIST:
        print(country)  