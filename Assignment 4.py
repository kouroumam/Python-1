
#Input: Prompt the user to enter the coordinates of two points in a 2D plane (x1, y1) and (x2, y2).
#Processing: Calculate the distance between the two points using the distance formula: Distance = sqrt((x2 - x1)^2 + (y2 - y1)^2).
#Output: Display the calculated distance between the two points.

#input
x1 = float(input("Enter x1 coordinate: "))
y1 = float(input("Enter y1 coordinate: "))
x2 = float(input("Enter x2 coordinate: "))
y2 = float(input("Enter y2 coordinate: "))

# Calculate the squared differences
dx_squared = (x2 - x1)  ** 2
dy_squared = (y2 - y1)  ** 2

distance_squared = dx_squared + dy_squared

distance = distance_squared ** 0.5

print("The distance between the points is: ", distance)
