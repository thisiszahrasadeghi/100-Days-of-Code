#Exercise 4.2
#Write a program which will select a random name from a list of names. the selected person will have to pay for everybody's food bill 😒 :


names_string = input ("Give me everybody's name , seperated by a comma. ")
names = names_string.split(",")
num_itmes = len(names)
import random

#With out using choise function :
'''random_integer = random.randint(0,num_itmes-1)
person = names[random_integer]
print(f"{person} is going to pay the bill! ")'''

#or just :
person = random.choice(names)
print(f"{person} is going to pay the bill! ")
