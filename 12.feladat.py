#első néhány fibonacci szám

def fibonacci(howMany):
    prev=0
    current=1
    for i in range(1,howMany):
        print(current)
        tmp = current
        current+=prev
        prev=tmp
        
        
fibonacci(int(input()))