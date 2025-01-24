

#Input: Prompt the user to enter a year.
#Processing: Determine whether the entered year is a leap year or not. A leap year is divisible by 4 but not by 100 unless it is also divisible by 400.
#Output: Display whether the entered year is a leap year or not.

year = int(input("Please type a year"))

# Check if the year is a leap year
# A leap year is divisible by 4
# But it should not be divisible by 100 unless it's also divisible by 400

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
