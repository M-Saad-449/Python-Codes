integer = int(input("Enter a number : "))
if(integer%2==0) and (integer%3==0):
    print("The number ",integer," is divisible of both 2 and 3")
elif (integer%3==0):
    print("The number ",integer," is divisible of 3 only")
elif (integer%2==0):
    print("The number ",integer," is divisible of 2 only")
    
else:
    print("The number",integer," is not a divisible of both 2 and 3")