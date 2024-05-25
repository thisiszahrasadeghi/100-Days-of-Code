#Exercise 3.5:
#Write a program that test the compatibility between two people based on BuzzFeed method.

print ("welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

'''name1 = name1.lower()
name2 = name2.lower()
T = name1.count("t") + name2.count("t")
R = name1.count("r") + name2.count("r")
U = name1.count("u") + name2.count("u")
E = name1.count("e") + name2.count("e")
L = name1.count("l") + name2.count("l")
O = name1.count("o") + name2.count("o")
V = name1.count("v") + name2.count("v")'''

# or just use one variable for name :
name = name1.lower() + name2.lower()
T = name.count("t")
R = name.count("r")
U = name.count("u")
E = name.count("e")
L = name.count("l")
O = name.count("o")
V = name.count("v")

true = T + R + U + E
love = L + O  + V + E

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90 :
    print(f"Your score is {love_score} , you go together like coke and mentos")

elif love_score >= 40 and love_score <= 50 :
    print(f"Your score is {love_score} , you are alright together")

else :
    print(f"Your score is {love_score}")
