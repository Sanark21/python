height = float (input())
weight = int(input())
bmi = weight / (height * height)
if bmi < 18.5:
    print( f"your BMI is {bmi}, you are underweight")
elif bmi < 25:
    print( f"your BMI is {bmi}, you are normalweight")
elif bmi < 30:
    print( f"your BMI is {bmi}, you are overweight")     
else:
    print("you BMI is extremely obese. start diet and excerise")

