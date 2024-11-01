integer = int(input("Enter a number : "))
if(integer%3==0) and (integer%5==0):
    print("The number ",integer," is multiple of both 3 and 5")
elif (integer%3==0):
    print("The number ",integer," is multiple of 3 only")
elif (integer%5==0):
    print("The number ",integer," is multiple of 5 only")
    
else:
    print("The number",integer," is not a multiple of both 3 and 5")