#a lépésköz előjele fogja eldönteni, melyik számtól melyik másik számig írok ki számot.
#A feladat szövege hibás, de messze túl későn csinálom ezt, hogy e miatt szólhassak önöknek
#most edge cases should be covered?
def betterAutoFor(start,finish,step):
    wrongOrder = (start < finish and step<0) or (start>finish and step>0)
    if wrongOrder:
        tmp = start
        start = finish
        finish = tmp
    for i in range(start,finish+1,step):
        print(i)
        
betterAutoFor(int(input("Egyik szám ")), int(input("Mésik szám ")),int(input("Lépésköz ")))