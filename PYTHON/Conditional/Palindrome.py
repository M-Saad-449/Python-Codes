Palindrome= str(input("Enter the palindrome sequence: "))
if Palindrome==Palindrome[::-1]:
    print("The given string "," ",Palindrome,"is a palindrome sequence")
else:
    print("The given sequence"," ", Palindrome,"is not a palindrome sequence")