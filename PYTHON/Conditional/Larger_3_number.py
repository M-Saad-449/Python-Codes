Num_1=int(input("Enter the first number : "))
Num_2=int(input("Enter the second number : "))
Num_3=int(input("Enter the third number: "))
if Num_1!=Num_2 or Num_1!=Num_3 or Num_2!=Num_3:
    print(max(Num_1,Num_2,Num_3))
else:
    print("All numbers are equal")