def factorial(theNumber):
    result=1
    for i in range(1,theNumber+1):
        result*=i
    return result

print(factorial(int(input("Hánynak a faktoriálisát keresed?"))))