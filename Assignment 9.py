



#Input: Ask the user to enter a single character.
#Processing: Determine whether the entered character is a vowel (a, e, i, o, u) or a consonant.
#Output: Display whether the entered character is a vowel or a consonant.

#Input
char = input("Please enter a single character: ")


#Processing
if len(char) == 1 and char.isalpha():
    # convert the letter to lowercase
    char = char.lower()

    #check if the char is a vowel
    if char in 'aeiou':
        print("The character is a vowel")
    else:
        print("THe character is a consonant! ")
else:
    if len(char) != 1:
        print("Error: Please enter only one character! ")
    else:
        print("Error: The input is not a letter")