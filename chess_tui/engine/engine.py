from stockfish import Stockfish
from chess_tui.screens.settings import getSkill


def engine(): 
    sf = Stockfish(path="/Users/abdel-rahmanmobarak/Desktop/stockfish/stockfish-macos-m1-apple-silicon")
    sf.set_skill_level(getSkill())
    print(getSkill())


    print(sf.get_board_visual())

    while True:
        myMove = input("Enter your move: ")
        if myMove == "quit":
            return

        if sf.is_move_correct(myMove) == True:
            sf.make_moves_from_current_position([myMove])
            computerMove = sf.get_best_move()

            print("Stockfish plays: ", computerMove)
            sf.make_moves_from_current_position([computerMove])

            sf.make_moves_from_current_position([myMove])
            print (sf.get_board_visual())
        else:
            print("Invalid move sequence!")