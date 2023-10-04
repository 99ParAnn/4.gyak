import math
def firstFewSquareNumbers(howMany):
    for i in range(howMany):
        print(pow(i+1,2), end=';')
    
firstFewSquareNumbers(10)