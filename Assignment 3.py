

#Input: Prompt the user to enter their weight in kilograms and height in meters.
#Processing: Calculate the BMI using the formula: BMI = Weight / (Height^2).
#Output: Display the calculated BMI.


weight = float(input("Enter your weight in Kilogram: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

#output
print("your BMI is: ", bmi)