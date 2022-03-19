
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

total = round(weight / (height * height))

if total < 18.5:
    print(f"Your BMI is {total}, you are underweight.")
elif total > 18.5 and total < 25:
    print(f"Your BMI is {total}, you have a normal weight.")
elif total > 25 and total < 30:
    print(f"Your BMI is {total}, you are slightly overweight.")
elif total > 30 and total < 35:
    print(f"Your BMI is {total}, you are obese.")
else:
    print(f"Your BMI is {total}, you are clinically obese.")
