


#Input: Prompt the user to enter their age.
#Processing: Classify the age into different categories:
#Under 18: Minor
#18-65: Adult
#Above 65: Senior citizen
#Output: Display the category based on the entered age.


#Input
age_input = input("Please enter your age: ")

# check if the input is a number and is not empty
if age_input.isdigit():
    age = int(age_input)

    #Ensure that the age is positive
    if age > 0:
        # start classification
        if age < 18:
            print("Minor")
        elif 18 <= age <= 65:
            print ("Adult")
        else:
            print("Senior Citizens")
    else:
        print("Error: Age must be a positive integer! ")

else:
    print("Error: Invalid input. Please enter a positive number")