def makeMove():
    myMove = input("Enter your move: ")
    return myMove

def resign():
    print("Game over, Stockfish wins!\n")

def chooseSide():
    while True:    
        try:
            choice = int(input("1. play white, 2. play black, 3. go back: "))
        except ValueError:
            print("Please enter a valid entry")

        if choice == 1:
            return "white"
        elif choice == 2:
            return "black"
        else:
            return   