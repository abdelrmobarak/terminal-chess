from chess_tui.screens.game import gameScreen, popLastResultMessage
from chess_tui.screens.settings import settings


class HomeScreen:
    def run(self):
        while True:
            if not self._showMenu():
                return

    def _printResultIfAny(self):
        lastResultMessage = popLastResultMessage()
        if lastResultMessage:
            print("\n" + lastResultMessage + "\n")

    def _readMenuOption(self):
        try:
            return int(input("1. play game, 2. edit skill level, 3. exit: "))
        except ValueError:
            print("Enter a valid option =(")
            return

    def _showMenu(self):
        self._printResultIfAny()
        print("terminal chess!")
        page = self._readMenuOption()
        if page is None:
            return True
        if page == 1:
            gameScreen()
            return True
        if page == 2:
            settings()
            return True
        if page == 3:
            return False
        print("Enter a valid option =(")
        return True
    
def home():
    HomeScreen().run()
