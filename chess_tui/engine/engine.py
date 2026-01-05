from stockfish import Stockfish
from chess_tui.screens.settings import getSkill, getDepth

def engine(): 
    sfEngine = Stockfish(path="/Users/abdel-rahmanmobarak/Desktop/stockfish/stockfish-macos-m1-apple-silicon")
    sfEngine.set_skill_level(getSkill())
    sfEngine.set_depth(getDepth())
    return sfEngine
