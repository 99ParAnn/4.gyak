import math

def autoFor(start,finish,step):
    for i in range(start,finish,step):
        print(i)
def numbersAndSquared(howMany):
    for i in range(howMany+1):
        print(f"{i}, {int(math.pow(i,2))}")
        #the pow function output float for me, and i found that ugly next to the ints
def firstExerciseThirdToLastPoint():
    for i in range(100,49,-5):
        print(i*2)
        #fuck i could have done this with AutoFor
        #leaving it here anyways
def firstExerciseSecondToLastPoint():
    print("1", end='')
    for i in range(2,1001):
        print(f", {i}", end='')
    else:
        print(".")
#ELSŐ FELADAT
#autoFor(0,51,1)
#autoFor(182,213,1)
#autoFor(100,201,2)
#autoFor(89,56,-2)
#numbersAndSquared(20)
#autoFor(99,0,-3)
#firstExerciseThirdToLastPoint()
#firstExerciseSecondToLastPoint()
#autoFor(1000,0,-3)
