from calendar import month_name
from signal import pthread_kill


print("Hello world" + ' '+"Hello World"+' '+"Hello World"+' '+"Hello World"+
' '+"I love python"+' '+"I love python"+' '+"I love python"+' '+"I love python")


def print_month_name(x):
    if (x==3) and (x==5):
        print("March" + "," + "May")
    if (x==6) and (x==8):
        print("June" + "," + "August")
    if (x==9) and (x==11):
        print("September" + "," + "November")
    if (x==12) and (x==2):
        print("December" + "," + "February")


month = int(input("Enter the month number: "))
print_month_name(month)