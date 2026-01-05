from chess_tui.screens.game import game
from chess_tui.screens.settings import settings

def home():
    while True:
        print("terminal chess!")
        try:
            page = int((input("1. play game, 2. edit skill level, 3. exit: ")))
        except ValueError:
            print("Enter a valid option =(")
            continue

        if page == 1:
            game()
        elif page == 2:
            settings()
        elif page == 3:
            return
        else:
            print("Enter a valid option =(")