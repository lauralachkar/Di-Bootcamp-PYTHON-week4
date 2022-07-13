
from ast import Str


string = str(input("Please enter a string:"))
len = len(string)

if len < 10:
    print("string not long enough")
elif len > 10:
    print("string too long ")

first_char = string[0]
last_char = string[-1]
print('First character:'+ first_char)
print('last character:'+ last_char)


string_to_iterate = string
for char in string_to_iterate[0]:
  print("First Character with loop:" + char)

for char in string_to_iterate[1]:
  print("Second Character with loop:" + char)  

for char in string_to_iterate[2]:
  print("Third Character with loop:" + char) 

for char in string_to_iterate[0 :-1]:
  print("Full String with loop:" + char)     