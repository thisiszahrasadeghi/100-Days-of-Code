#Exersice 2:
#Write a program using maths and f-string that tells us how many days , weeks and months we have left if we live until 90 years old.

age = input("what is your current age?")
int_age = int(age)
rest_year = 90 - int_age
days = rest_year * 365
weeks = rest_year * 52
months = rest_year * 12
print(f" you have {days} days , {weeks} weeks and {months} months left")
