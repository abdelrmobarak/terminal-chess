from stockfish import Stockfish
from chess_tui.screens.settings import getSkill, getDepth

def engine(): 
    sfEngine = Stockfish(path="{YOUR PATH}")
    sfEngine.set_skill_level(getSkill())
    sfEngine.set_depth(getDepth())
    return sfEngine
