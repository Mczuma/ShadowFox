height= float(input("Enter height in meters: "))
weight= float(input("Enter weight in kilograms: "))

bmi = weight / (height**2)
if bmi >= 30:
    print("obesity")
elif bmi>= 25:
    print("overweight")
elif bmi>= 18.5:
    print("Normal")
else:
    print("Underweight")