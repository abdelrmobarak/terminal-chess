import chess
from rich.text import Text
from textual.app import App
from textual.containers import Vertical
from textual.widgets import Footer, Header, Input, Static
from chess_tui.engine.engine import engine

lightSquare = "#f0d9b5"
darkSquare = "#b58863"
whitePiece = "bold white"
blackPieceLight = "bold black"
blackPieceDark = "bold gray23"
pieceSymbols = {}
files = "abcdefgh"
squareWidth = 5
labelWidth = 3
lastResultMessage = None

class TextualChess(App):
    bindings = [("q", "quit", "Quit")]
    def __init__(self):
        super().__init__()
        self.stockfish = engine()
        self.playerSide = None
        self.logMessages: list[str] = []

    def compose(self):
        yield Header()
        with Vertical(id="layout"):
            yield Static(id="board")
            yield Static(id="log")
            yield Input(
                placeholder="Choose side: white/black. Once started, enter moves like e2e4.",
                id="prompt",
            )
        yield Footer()

    def on_mount(self):
        self._updateBoard()
        self._appendMessage("Choose a side to begin.")

    def on_input_submitted(self, event: Input.Submitted):
        value = event.value.strip().lower()
        event.input.value = ""
        if not value:
            return

        if self.playerSide is None:
            self._handleSideSelection(value)
            return

        if value in {"resign", "quit", "exit"}:
            self._endGame("You resigned")
            return

        if not self.stockfish.is_move_correct(value):
            self._appendMessage("Invalid move. Try again.")
            return

        self.stockfish.make_moves_from_current_position([value])
        self._appendMessage(f"You played: {value}")
        self._updateBoard()
        if self._checkGameEnd():
            return
        self._playEngineMove()

    def _handleSideSelection(self, value: str):
        if value in {"white", "w"}:
            self.playerSide = "white"
            self._appendMessage("You are playing white.")
            self._updateBoard()
            return
        if value in {"black", "b"}:
            self.playerSide = "black"
            self._appendMessage("You are playing black.")
            self._playEngineMove()
            return
        self._appendMessage("Please enter 'white' or 'black'.")

    def _playEngineMove(self):
        computerMove = self.stockfish.get_best_move()
        if not computerMove:
            self._endGame("Stockfish has no legal moves.")
            return
        self.stockfish.make_moves_from_current_position([computerMove])
        self._appendMessage(f"Stockfish plays: {computerMove}")
        self._updateBoard()
        self._checkGameEnd()

    def _appendMessage(self, message: str):
        self.logMessages.append(message)
        self.logMessages = self.logMessages[-6:]
        log = self.query_one("#log", Static)
        log.update("\n".join(self.logMessages))

    def _updateBoard(self):
        board = self.query_one("#board", Static)
        board.update(self._renderBoard())

    def _renderBoard(self):
        text = Text()
        for rankIndex, rankData in enumerate(self._fenToRanks()):
            rankNumber = 8 - rankIndex
            pieces = self._expandRank(rankData)
            self._renderRankRow(text, rankNumber, pieces, show_label=True)
            spacer = [" "] * len(pieces)
            self._renderRankRow(text, rankNumber, spacer, show_label=False)
        text.append(" " * labelWidth, style="bold")
        for fileLetter in files:
            text.append(fileLetter.center(squareWidth), style="bold")
        return text

    def _renderRankRow(self, text: Text, rankNumber: int, pieces, show_label: bool):
        label = str(rankNumber).center(labelWidth) if show_label else " " * labelWidth
        text.append(label, style="bold")
        for fileIndex, piece in enumerate(pieces):
            self._appendSquare(text, piece, rankNumber, fileIndex)
        text.append("\n")

    def _appendSquare(self, text: Text, piece: str, rank: int, fileIndex: int):
        isDark = (rank + fileIndex) % 2 == 1
        background = darkSquare if isDark else lightSquare
        if piece == " ":
            text.append(" " * squareWidth, style=f"on {background}")
            return
        pieceStyle = whitePiece if piece.isupper() else (
            blackPieceDark if isDark else blackPieceLight
        )
        symbol = pieceSymbols.get(piece, piece)
        text.append(symbol.center(squareWidth), style=f"{pieceStyle} on {background}")

    def _checkGameEnd(self):
        board = chess.Board(self.stockfish.get_fen_position())
        if board.is_checkmate():
            winner = "Black" if board.turn == chess.WHITE else "White"
            if self.playerSide == winner.lower():
                self._endGame("Checkmate, You win")
            else:
                self._endGame("Checkmate, Stockfish wins")
            return True
        if board.is_stalemate():
            self._endGame("Stalemate. Draw.")
            return True
        return False

    def _endGame(self, message: str):
        global lastResultMessage
        self._appendMessage(message)
        lastResultMessage = message
        self.exit()

    def _fenToRanks(self):
        fen = self.stockfish.get_fen_position()
        boardPart = fen.split(" ")[0]
        return boardPart.split("/")

    def _expandRank(self, rankData):
        pieces = []
        for token in rankData:
            if token.isdigit():
                pieces.extend([" "] * int(token))
            else:
                pieces.append(token)
        return pieces


def gameScreen():
    TextualChess().run()

def popLastResultMessage():
    global lastResultMessage
    message = lastResultMessage
    lastResultMessage = None
    return message
