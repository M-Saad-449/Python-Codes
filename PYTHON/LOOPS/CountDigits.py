Number = int(input("Enter the number : "))
Number = abs(Number)
if (Number == 0):
    count  = 1
else:
    count = 0
while Number>0:
    Number //=10
    count+=1
    
print(count)