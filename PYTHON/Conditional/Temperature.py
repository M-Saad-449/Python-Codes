Temperature = float(input("Enter the temperature in celcius : "))
if Temperature <= 0:
    print("It is freezing poiint")
elif Temperature<=37 and Temperature>0:
    print("It is moderate")
elif Temperature<=60 and Temperature>37:
    print("It is moderately warm")
elif Temperature<=90 and Temperature>60:
    print("it is extremely warm")
else:
    print("It is boiling")