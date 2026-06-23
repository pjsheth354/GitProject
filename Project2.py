#Choosing a number to find the area of rectangle, square and right angle triangle

def areaofrectangle(length,breadth):
    area = float(length) * float(breadth)
    print("The Area of Rectangle is: {}".format(area))

def areaofsquare(length):
    area = float(length) * float(length)
    print("The Area of Sqaure is: {}".format(area))

def areaoftriangle(base,height):
    area = (1/2) * float(base) * float(height)
    print("The Area of Triangle is: {}".format(area))

print("""Choose an option to calculate area for:
        1 - Rectangle
        2 - Square
        3 - Triangle
      """)

num = int(input("Enter your option: \n"))

if (num == 1):
    length = float(input("Enter the length of Rectangle:\n"))
    breadth = float(input("Enter the breadth of Rectangle:\n"))
    areaofrectangle(length,breadth)
elif (num == 2):
    length = float(input("Enter the length of Square:\n"))
    areaofsquare(length)
elif (num == 3):
    base = float(input("Enter the base of Triangle:\n"))
    height = float(input("Enter the height of Triangle:\n"))
    areaoftriangle(base,height)
else:
    print("You entered a wrong option")