

#Develop a function named power that takes two integers, base and exponent, as input and returns base raised to the power of exponent.


def power(base, exponent):
    result = 1

    if exponent == 0:
        return 1

    if exponent > 0:
        for _ in range(exponent):
            result = result * base
        return result

    if exponent < 0:
        for _ in range(-exponent):
            result = result * base
    return 1 / result

base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))
result = power(base, exponent)
print(f"{base} raised to the power of {exponent} is: {result}")

