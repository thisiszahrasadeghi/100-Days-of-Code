#exercise 3.3
#Write a program that works out if a given year is leap year.

year = int(input("which year do you want to check? "))
remain_4 = year % 4
remain_100 = year % 100
remain_400 = year % 400
if remain_4 == 0:
    if remain_100 == 0:
        if remain_400 == 0:
            print("Leap year.")
        else:
            print("Not leap year!")
    else:
        print("Leap year.")
else:
    print("Not leap year!")
