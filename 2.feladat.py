def repeatedPrint(howMany, what):
    for i in range(howMany):
        print(what, end='')

def makeStarryBorder(text):
    howManyStars= len(text)+4
    for i in range(howManyStars):
        print('*', end='')
    print(f"\n* {text} *")
    for i in range(howManyStars):
        print("*", end='')
    
def chessboard():
    startsWithSpace=False
    for i in range(8):
        if startsWithSpace:
            print(' '*1, end='')
            startsWithSpace = False
        else:
            startsWithSpace = True
        for j in range(4):
            print('*', end=' ')
        print()
        
#repeatedPrint(100,'*')

#repeatedPrint(int(input("Hány karaktert írjak ki?")), input("Melyik karaktert írjam ki ennyiszer?"))

#makeStarryBorder(input("A szöveget, amit megadsz, bekeretezem csillagokkal"))

#chessboard()

