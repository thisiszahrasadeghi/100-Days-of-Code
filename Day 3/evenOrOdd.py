#exersice 3.1:
#Write a program that figure out if a given number is an odd or even number.

number = int(input("which number do you want to check? "))
remaining = number % 2
if remaining == 0:
    print("this is an even number")
else:
    print("this is an odd number")
