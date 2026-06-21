#String Operations

str1 = "Hello"
str2 = " My Name is Priyam "
str3 = "Have a Good Day!!"
str4 = """
    This is a case 1
    This is a case 2
    This is a case 3
"""
#String Slicing 
print(str1[1:]) #1 to all
print(str1[:3]) #Start all to 3(Not Included) 
print(str1[2:4]) # 2 to 4(Not Included)
print(str1[-3:-1]) #-3 to -1(Not Included)


print(str1 + " " + str2 + " "+ str3)
print(str1.capitalize())
print(str1.upper())
print(str1.lower())
print(str2.strip()) #Removes White Spaces from the beginning or end
print(str3.split(" ")) #Returns a list but just provide a separator
print(str1.swapcase())
print(str1.title())
print(str1.center(24)) #Gives the spacing in the code
print(str4.count("case")) #Input the word need to count in the sentence
print(str4.replace("case","line"))
print(str4.casefold()) #Casefold converts uppercase letter to lowercase including some special characters which are not specified in the ASCII table

#Format String
#Method 1
age = 30
str5 = f"My age is {age:.2f}" #Can perform math or use modifier to format the value
print(str5)

#Method2
ageAbove = 25
str6 = "My age is {}"
print(str6.format(ageAbove))

#Escape Character
print("Hello World, My Name is \"Priyam\" ")

#Other Methods are available but no need to remember search it if you need it.