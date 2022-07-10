# Exercise 1

from tokenize import Exponent


print("Hello world" +' '+ 
"Hello world"+ '' + " Hello word" + '' + "Hello word")

# Exercise 2

base = 99
exponent = 3
print("The final value is: ",pow(base,exponent)*8)


# Exercise 3

 # 5 < 3
 # The outcome will be true 

#3 == 3
#The outcame will be true

#3 == "3"
#The outcame will be false

#"Hello" == "Hello"
#The outcome will be true

#Exercise4

computer_brand = "MacBook"
print("I have a " +''+ computer_brand)

#Exercise5

name = "laura"
age = str(25)
shoe_size =str(39)
info = "My name is" +' '+ name + "," + age + "and my shoe size is"+' '+ shoe_size
print(info)

#Exercise6

a = 130
b = 100

if(a > b):
    print("Hello World")


#Exercise 7

num = int(input("Enter any number to test whether it is odd or even : "))

if(num % 2) == 0:
    print("The number is even")
else:
    print("The nmber is odd")    


 #Exercise 8

name = str(input("Enter your name"))
my_name = "laura"

if name != my_name:
    print("we have the same name so funny")


#Exercise 8

h_height = int(input("Please enter your height: "))
h_ft = int(input("Feet: "))
h_inch = int(input("Inches: "))
h_inch += h_ft * 12

h_cm = round(h_inch*2.54,1)

if h_cm > 145:
    print("You're enought to ride")
else:
    print("You need to grow more to ride!!!")    