side1 = float(input("Enter the first side of the trianle: "))
side2 = float(input("Enter the second side of the trianle: "))
side3 = float(input("Enter the third side of the trianle: "))

if(side1+side2>side3) and (side3+side1>side2) and (side2+side3>side1):
    print("They form the triangle")
else:
    print("They donot form the side of the triangle")