import math
def intervalSquareRoot(start,finish):
    if start>finish:
        tmp = start
        start = finish
        finish = tmp
    for i in range(start,finish+1):
        print(round(pow(i,0.5),2))
        
        
intervalSquareRoot(int(input("egyik szám")),int(input("másik szám")))