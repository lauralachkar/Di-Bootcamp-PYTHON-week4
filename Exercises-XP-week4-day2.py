#Exercise 1

from unicodedata import name


my_fav_numbers = {20,30,10,5,40}
my_fav_numbers.add(100)
my_fav_numbers.add(120)
print(my_fav_numbers)

remove = my_fav_numbers.pop()
print(remove)

friend_fav_number = {200,250,300,500}
join = my_fav_numbers.union(friend_fav_number)
print(join)

#Exercise 3

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append('Kiwi')
basket.insert(0, "Apples")
print(basket)

count_apple = basket.count("Apples")
print(count_apple)

basket.clear()
print(basket)


#Exercise 4

#A floar is a decimal number .On the opposite an integer is a whole number without any decimal value
#Another way to generate a float is to use arrange or /10
#[] is to generate a list


#Exercise 5

for i in range(1, 20):
    print(i)

    start, end = 1, 20
    for num in range(start, end + 1):
         if num % 2 == 0:
            print(num, end = "Even Numbers")

 #The end parameter is used to append any string at the end of the output of the print statement in python.

 #Exercise 6


keep_going = True
while keep_going:
     name = input('Enter your name, or type quit to exit ')
     if name == "laura":
        keep_going = False


#Exercise 7

fruits_ls = []


def add_fruits():
    while True:
        print("choose your favorite fruits:\n"
            "1- apple\n"
            "2- orange\n"
            "3- kiwi\n"
            "4- exit\n")

        my_fruits = input()
        if my_fruits == str(1) or my_fruits == "apple":
            fruits_ls.append("Apple")
        elif my_fruits == str(2) or my_fruits == "orange":
            fruits_ls.append("Orange")
        elif my_fruits == str(3) or my_fruits == "kiwi":
            fruits_ls.append("Kiwi")
        elif my_fruits == str(12) or my_fruits == "appleorange" or my_fruits == str(21) or my_fruits == "orangeapple":
            fruits_ls.append("Apple")
            fruits_ls.append("Orange")

        elif my_fruits == str(13) or my_fruits == "applekiwi" or my_fruits == str(31) or my_fruits == "kiwiapple":
            fruits_ls.append("Apple")
            fruits_ls.append("Kiwi")

        elif my_fruits == str(23) or my_fruits == "orangekiwi" or my_fruits == str(32) or my_fruits == "kiwiorange":
            fruits_ls.append("Orange")
            fruits_ls.append("Kiwi")

        elif my_fruits == str(4) or my_fruits == "exit":
            print("You chose a new fruit. I hope you enjoy")
            break


add_fruits()

print(fruits_ls)

