from stockfish import Stockfish
from ..screens.settings import elo

sf = Stockfish(path="your-path-here")

sf.set_elo_rating(elo)

print(sf.get_board_visual())

while True:
    print('Enter move: ')
    myMove = input()

    sf.make_moves_from_current_position([myMove])

    computerMove = sf.get_best_move()
    print("Stockfish plays: ", computerMove)

    sf.make_moves_from_current_position([computerMove])
    print (sf.get_board_visual())