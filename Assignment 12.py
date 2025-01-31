

#Description: Develop a program that prompts the user to enter the number of rows for a pattern and then prints a pattern of asterisks (*) in the form of a right triangle.

# create a nested loop to check a valid input

 # ask the user to enter the number of rows
rows = int(input("Enter the number of rows for the triangle: "))

# create the triangle using a nested loop
for i in range(1, rows + 1):
    for j in range(i):
        print('*', end='')
    print()