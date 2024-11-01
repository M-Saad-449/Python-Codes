a = int(input("Enter the one side : "))
b = int(input("Enter the 2nd side : "))
c = int(input("Enter the 3rd side : "))
if a==b==c:
    print("The Given Triangle is equilateral")
elif a==b or b==c or a==c:
    print("The given triangle is iosceles")
else:
    print("Te gievn triangle is scalene")