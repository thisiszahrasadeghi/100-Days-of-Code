#Day 2 Project:
#Write a program that calculate the tip you have to pay

bill = float(input("what's total bill? $"))
tip = int(input("what percentage tip would you like to givr? 10,12 or 15?"))
people = int(input("how many people to split the bill?"))
bill_as_int += tip_as_int * 0.01 * bill_as_int 
#bill_with_tip = tip_as_int / 100 * bill_as_int + bill_as_int 
#tip_as_int / 100 * bill_as_int + bill_as_int as the same as : bill_as_int * ( 1 + tip_as_int / 100)
ech_person = bill_as_int / people_as_int
round_each_person = round(ech_person ,2)
message = f"each person sould pay ${round_each_person}"
print(message)
