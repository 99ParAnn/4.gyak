#1*2 + 2*3 + ... + K * (k+1)

def myFunction(K):
    result=0
    for i in range(1,K+1):
        result+= i*(1+i)
    return result

print(myFunction(int(input())))