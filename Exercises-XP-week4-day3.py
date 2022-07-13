#Exercise 1

from datetime import date
import fractions
from operator import le
from os import major
from turtle import back
from types import FrameType
from unicodedata import name


keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

keys_dictionnary = dict(zip(keys,values))
print(keys_dictionnary)

family_member = list(keys_dictionnary.values())
print("cost of each famyliy member:" + str(family_member))


#Exercise 2

# name: Zara 
#creation_date: 1975 
#creator_name: Amancio Ortega Gaona 
#type_of_clothes: men, women, children, home 
#international_competitors: Gap, H&M, Benetton 
#number_stores: 7000 
#major_color: 
    #France: blue, 
    #Spain: red, 
    #US: pink, green


brand = {
    "name" : "Zara",
    "creation_date" : 1975,
    "creation_name" : "Amancio Ortega Gaona",
    "type_of_clothes" : "men,women,children,home",
    "international_competitors": "Gap, H&M, Benetton",
    "number_stores" : 7000,
    "major_color" :{
        "France" : "blue",
        "Spain" : "red",
        "US" : "pink,green"
    }
}

brand["number_stores"] = 2
print(brand)


Zara_clients = [key for key in brand.keys()][3], [value for value in brand.values()][3]
print("Zara clients are:"+str(Zara_clients)) 

brand["country_creation"]= "Spain"
print("after adding a key and value:"+str(brand))

key_to_lookup = 'international_competitors'
brand['international_competitors'] = "Desigual"
if key_to_lookup in brand:
    print(brand)
else:
    print(f"No, key: '{key_to_lookup}' does not exists in dictionary")


del brand["creation_date"]
print("Dictionary after del: "+str(brand)) 

last_value = list(brand.values())[3]
print("The last key of international_competitors: " + str(last_value))


major_colors = brand["major_color"]['US']
print("the major clothes colors:" + major_colors)


length = len(brand)
print("Length of dictionary:",length)


more_on_zara = {
    "creation_date" : 1975,
    "number_stores" : 10000,
}

brand.update(more_on_zara)
print("added dictionnary:",brand)

