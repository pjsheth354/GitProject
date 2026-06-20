#String Operations

str1 = "Hello"
str2 = "My Name is Priyam"
str3 = "Have a Good Day!!"
str4 = """
    This is a case 1
    This is a case 2
    This is a case 3
"""

print(str1 + " " + str2 + " "+ str3)
print(str1.capitalize())
print(str1.upper())
print(str1.lower())
print(str1.swapcase())
print(str1.title())
print(str1.center(24)) #Gives the spacing in the code
print(str4.count("case")) #Input the word need to count in the sentence
print(str4.replace("case","line"))
print(str4.casefold()) #Casefold converts uppercase letter to lowercase including some special characters which are not specified in the ASCII table
print(str4.format())
