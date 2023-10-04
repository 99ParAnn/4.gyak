#prímszámok

import math

def primes(howMany):
    current=1
    for i in range(howMany):
        current+=1
        foundIt=False
        while not foundIt:
            current+=1
            if isItPrime(current):
                foundIt = True
                print(current)

        
def isItPrime(num):
        isPrime=True
        for j in range(math.ceil(pow(num,0.5)), 1,-1):
            if num % j == 0:
                isPrime=False                
        return isPrime

primes(int(input()))
