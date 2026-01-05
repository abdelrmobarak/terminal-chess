from chess_tui.engine.engine import engine
from chess_tui.app.actions import *

def game():
    sf = engine()
    side = chooseSide()  

    while True:
        print(sf.get_engine_parameters())
        print(sf.get_board_visual())
        
        if side == "black": # If the user is playing black
            computerMove = sf.get_best_move()
            print("Stockfish plays: ", computerMove)
            sf.make_moves_from_current_position([computerMove])
            print (sf.get_board_visual(False))
            myMove = makeMove()

            if myMove == "resign":
                resign()
                return
            
            if sf.is_move_correct(myMove) == True:
                sf.make_moves_from_current_position([myMove])
                print (sf.get_board_visual(False))
            else:
                print("Invalid move sequence!")
        
        else: # If the user is playing white
            myMove = makeMove()
            if myMove == "resign":
                resign()
                return            
            if sf.is_move_correct(myMove) == True:
                sf.make_moves_from_current_position([myMove])
                computerMove = sf.get_best_move()
                print("Stockfish plays: ", computerMove)
                sf.make_moves_from_current_position([computerMove])
                print (sf.get_board_visual())
            else:
                print("Invalid move sequence!")

