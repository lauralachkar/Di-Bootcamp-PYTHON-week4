from cgitb import text
from crypt import crypt
from gettext import npgettext
from hashlib import scrypt
import math
from ssl import _PasswordType
from this import s

#Exercise 1

list = ["apples","banana"]
list.insert(0,"abc")
print(list)

#Exercise 2

# create function that
# return space count
def check_space(string):
     
    # counter
    count = 0
     
    # loop for search each index
    for i in range(0, len(string)):
         
        # Check each char
        # is blank or not
        if string[i] == " ":
            count += 1
         
    return count

string = "Welcome in challenge's day"
print("number of spaces",check_space(string))


#Exercise 3 

input = input("Please enter a word:")
count_uppercase = 0
count_lowercase = 0

for i in input:
      if(i.isupper()):
            count_uppercase=count_uppercase+1
      elif(i.islower()):
          count_lowercase=count_lowercase+1     

print("The number of uppercase characters is:",count_uppercase)
print("The number of lowercase characters is:",count_lowercase)             
        
#Exercise 4

arr = [10, 200, 20, 40.5, 5]

def _sum(arr):
 
    sum = 0
 
    for i in arr:
        sum = sum + i
 
    return(sum)

ans = _sum(arr)
print('Sum of the array is ', ans)

#Exercise 5

numbers = [456, 700, 200,300,1000]
max_number = max(numbers)
print("max number in the list",max_number)

#Exercise 6

def factorial(x):
    return math.factorial(x)
 
print("factorial number:",factorial(5))

#Exercise7

list_a = ["Hello", 2, 15, "World", 34]
number_of_elements = len(list_a)

print("Number of elements in the list: ", number_of_elements)

#Exercise 9

def ismonotone(a):
    n=len(a) #size of array
    if n==1:
        return True
    else:
        #check for monotone behaviour
        if all(a[i]>=a[i+1] for i in range(0,n-1) or a[i]<=a[i+1] for i in range(0,n-1)):
            return True
        else:
            return False

A = [6, 5, 4, 2]
print(ismonotone(A))


#An array is said to be monotonic in nature if the array elements 
# are continuously increasing or continuously decreasing.

#Exercise 10

a_list = ["a_string", "the_longest_string", "string"]
longest_string = max(a_list, key=len)
print("the longest word in the list:",longest_string)

#Exercise 11

strings_numbers_list = ['1 2 3', '4 5 6', 'invalid','valid']
numbers = []
for item in strings_numbers_list:
    for subitem in item.split():
        if(subitem.isdigit()):
            numbers.append(subitem)
print(numbers)


#The isdigit() method returns True if all the characters are digits, otherwise False.
#Exponents, like ², are also considered to be a digit.


#Exercise 12

a_string = 'Was it a car or a cat I saw'
def palindrome(string):
    string = string.lower().replace(' ', '')
    return string == string[::-1]
print(palindrome(a_string))


#We then re-assign the string to itself, but lower all the character cases and remove any spaces
#We then return the evaluation of whether the string is equal to itself, backwards
#This returns True if the string is a palindrome, and False if it is not

#Exercise 13

def word_k(k, s):    
    # split the string where space comes
    word = s.split(" ")
    # iterate the loop for every word
    for x in word:
        # if length of current word
        if len(x)>k:
          # greater than k then
          print(x)
k = 3
s ="Python is good"
word_k(k, s)


#Exercise 14

dict_avg=({'a': 1,'b':2,'c':8,'d': 1})
filtered_vals = [v for _, v in dict_avg.items() if v != 0]
average = sum(filtered_vals) / len(filtered_vals)
print(average)

#You can do this by iterating over the dictionary and filtering out zero values first. Then take the sum of the filtered values. Finally, divide by the 
# number of these filtered values. 

#Exercise 15


def ngcd(x, y):
    i=1
    while(i<=x and i<=y):
        if(x%i==0 and y%i == 0):
            gcd=i
        i+=1
    return gcd
def num_comm_div(x, y):
  n = ngcd(x, y)
  result = 0
  z = int(n**0.5)
  i = 1
  while( i <= z ):
    if(n % i == 0):
      result += 2 
      if(i == n/i):
        result-=1
    i+=1
  return result

print("Number of common divisors: ",num_comm_div(2, 4))

#Exercise 16

num = 29
flag = False

if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")

#Numbers less than or equal to 1 are not prime numbers. Hence, we only 
# proceed if the num is greater than 1.We check if num is exactly divisible by any number from 2 to num - 1. If we find a factor in that range, the number is not prime, so we set 
# flag to True and break out of the loop.

#Exercise 17

weird_print=([1,2,2,3,4,5])
print('Printing the List Items at Even Position')
print(weird_print[1:len(weird_print):2])

#Exercise 19

string = "Python is a fun programming language"
result = string.split()
print(result)
