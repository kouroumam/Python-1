



#Input: Prompt the user to enter a time duration in hours.
#Processing: Convert the time duration to minutes and seconds.
#Output: Display the converted time duration in minutes and seconds.


# Input: Ask the user to enter a time duration in hours
hours = float(input("Enter the time duration in hours: "))

# Processing: Convert hours to minutes and seconds
minutes = hours * 60
seconds = hours * 3600

# Output: Display the converted time duration
print(f"{hours} hour(s) is equal to:")
print(f"{int(minutes)} minutes")
print(f"{int(seconds)} seconds")