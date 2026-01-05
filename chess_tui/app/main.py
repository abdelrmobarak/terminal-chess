from chess_tui.engine.engine import engine
from chess_tui.screens.settings import changeSkill

def main():
    while True:
        print("terminal chess!")
        try:
            page = int((input("1. play game, 2. edit skill level, 3. exit: ")))
        except ValueError:
            print("Enter a valid option =(")
            continue
    
        if page == 1:
            engine()
        elif page == 2:
            changeSkill()
        elif page == 3:
            return
        else:
            print("Enter a valid option =(")



main()