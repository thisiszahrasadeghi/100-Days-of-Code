#Exersice 3.2:
#write a program that interprets the BMI based on a user's wight and height.
#❗you should round the result to nearst whole number.

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
BMI = weight / height ** 2
result = round(BMI)
print(result)
if result<18.5:
    print(f"Your BMI is {result} , you are underweight.")
elif result>=18.5 and resault<25:
    print(f"Your BMI is {result} , you are normal weight.")
#because she didn"t teach the and/or she did this:
#elif result<25
elif result>=25 and resault<30:
    print(f"Your BMI is {result} , you are overweight.")
#elif result<30
elif result>=30 and resault<35:
    print(f"Your BMI is {result} , you are obese.")
#elif result<35
else:
    print(f"Your BMI is {result} , you are clinically obese.")
