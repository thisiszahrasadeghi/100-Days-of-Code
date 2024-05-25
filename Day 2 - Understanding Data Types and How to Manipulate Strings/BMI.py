#Exercise 1:
#Write a program that calculates the Body Mass Index(BMI) from user's weight and height.

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
BMI = float(weight) / float(height)**2
#print(type(BMI))
print("your BMI is: " + str(BMI))