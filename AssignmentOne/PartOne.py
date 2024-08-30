height = float(input("Enter your height in inchies"))
weight = float(input("Enter your weight"))

BMI = (weight * 703) / (height **2)

print(BMI)

if BMI <= 18.5:
    print("You are underweight")
elif BMI >= 25:
    print("You are overweight")
else:
    print("You are at a optimal weight")
