#három összes olyan többszöröse, ami kisebb-egyenlő
#a feladat hibás; az összes pozitív többszöröst íratom ki
def multiplesOfThreeUpTo(upperLimit):
    for i in range(3,upperLimit+1, 3):
        print(i)
        
multiplesOfThreeUpTo(int(input()))