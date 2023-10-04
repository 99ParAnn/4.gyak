#n-nél nem nagyobb páratlan számok összege
#nem vagyok elég éber beszédes nevet adni neki
def myFunction(n):
    sum = 0
    for i in range(1,n+1,2):
        print(i)
        
myFunction(16)

myFunction(int(input("n?")))