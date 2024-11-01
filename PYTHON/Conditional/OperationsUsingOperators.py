num_1 = float(input("Enter the first integer: "))
num_2 = float(input("Enter the second integr: "))
operators = input("Enter an operator: ")
if operators == '+':
    result = num_1+num_2
elif operators == '-':
    result = num_1-num_2
elif operators == '*':
    result = num_1*num_2
elif operators == '/':
    result = num_1/num_2
else:
    print("Inavid operator")
print(result)

        