from games import *

class GameOfNim(Game):
    """Play Game of Nim with first player 'MAX'."""

    def __init__(self, board=[3,1]):
        """Initialize the game with a given board state."""
        self.initial = GameState(to_move='MAX', utility=0, board=board, moves=self.get_moves(board))

    def get_moves(self, board):
        """Generate valid moves."""
        return [(r, n) for r, count in enumerate(board) for n in range(1, count + 1)]

    def actions(self, state):
        """Return valid moves."""
        return state.moves

    def result(self, state, move):
        """Apply move and return new state."""
        r, n = move
        board = list(state.board)
        board[r] -= n
        return GameState(to_move='MIN' if state.to_move == 'MAX' else 'MAX',
                         utility=self.utility(state, state.to_move),
                         board=board,
                         moves=self.get_moves(board))

    def utility(self, state, player):
        """Return 1 if MAX wins, -1 if MIN wins, else 0."""
        return 1 if self.terminal_test(state) and state.to_move == 'MIN' else -1 if self.terminal_test(state) else 0

    def terminal_test(self, state):
        """Check if game is over."""
        return all(pile == 0 for pile in state.board)

    def display(self, state):
        """Show board."""
        print("board:", state.board)


if __name__ == "__main__":
    nim = GameOfNim(board=[7, 5, 3, 1])
    print(nim.initial.board)
    print(nim.initial.moves)

    mode = input("Choose game mode: (1) Human vs AI, (2) Human vs Human: ").strip()
    utility = nim.play_game(alpha_beta_player if mode == "1" else query_player, query_player)

    print("MIN won the game" if utility < 0 else "MAX won the game")
2
