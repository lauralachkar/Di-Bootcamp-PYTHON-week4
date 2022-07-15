#Exercise 1

import numbers
import random

from pip import main


def display_message():
    print("we learn programmation languages : HTML/CSS")

display_message()

#Exercise 2

def favorite_book(title):
     print(f"One of my favorite books is {title}")

favorite_book("Narnia")

#Exercise 3

def favorite_book(city,country):
    print(city,f"is in {country}")

favorite_book("england","United Kingdom")

#Exercise 6

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians():
    print(magician_names,sep=',')

show_magicians()

def make_great():
    print(['The great {0}'.format(i) for i in magician_names])

make_great()

def final_sentence():
  make_great()

final_sentence()
