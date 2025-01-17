

#Input: Prompt the user to enter the principal amount, interest rate (in percentage), and the time period (in years).
#Processing: Calculate the simple interest using the formula: Simple Interest = (Principal * Rate * Time) / 100.
#Output: Display the calculated simple interest.


principal = float(input("Enter the principal amount: "))

rate = input("Enter the interest rate: ")
interest_rate = float(rate)


time = float(input("Enter the time period: "))


simple_interest = (principal * interest_rate * time) / 100
print("The calculated simple interest is: ", simple_interest)

nj