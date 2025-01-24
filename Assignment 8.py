

#Input: Ask the user to enter their marks for three subjects.
#Processing: Calculate the average of the marks. Determine the grade based on the average:
#90 and above: A
#80-89: B
#70-79: C
#60-69: D
#Below 60: F
#Output: Display the calculated grade.

mark1 = int(input("Enter your marks for Subject 1: "))
mark2 = int(input("Enter your marks for Subject 2: "))
mark3 = int(input("Enter your marks for Subject 3: "))

# Average
average = (mark1 + mark2 + mark3) / 3

# Step 3: Determine the grade based on the average
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

#Output
print(f"Your grade is: {grade}")