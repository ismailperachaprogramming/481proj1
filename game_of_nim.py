from games import *

class GameOfNim(Game):
    def __init__(self, board=[3, 1]):
        self.initial = GameState(to_move='MAX', utility=0, board=board, moves=self._generate_moves(board))

    def _generate_moves(self, board):
        """Generates all possible moves for the given board state."""
        moves = []
        for i, row in enumerate(board):
            if row > 0: 
                for j in range(1, row + 1):
                    moves.append((i, j))
        return moves

    def actions(self, state):
        """Legal moves are at least one object, all from the same row."""
        return state.moves

    def result(self, state, move):
        """Returns the state that results from making a move from a state."""
        if move not in state.moves:
            raise ValueError("Invalid move")
        row, num_objects = move
        new_board = state.board.copy()
        new_board[row] -= num_objects
        new_moves = self._generate_moves(new_board)
        new_player = 'MIN' if state.to_move == 'MAX' else 'MAX'
        if sum(new_board) == 0:
            utility = 1 if state.to_move == 'MAX' else -1
        else:
            utility = 0
        return GameState(to_move=new_player, utility=utility, board=new_board, moves=new_moves)

    def utility(self, state, player):
        """Returns the value to player; 1 for win, -1 for loss, 0 otherwise."""
        return state.utility if player == 'MAX' else -state.utility

    def terminal_test(self, state):
        """A state is terminal if there are no objects left."""
        return sum(state.board) == 0

    def display(self, state):
        """Displays the current state of the game."""
        board = state.board
        print("board: ", board)

if __name__ == "__main__":
    nim = GameOfNim(board=[7, 5, 3, 1])  
    print("Initial board:", nim.initial.board)  # must be [7, 5, 3, 1]
    print("Initial moves:", nim.initial.moves)  # must be [(0, 1), (0, 2), ..., (3, 1)]
    print("Resulting state after move (0, 1):", nim.result(nim.initial, (0, 1)))

    utility = nim.play_game(alpha_beta_player, query_player) 
    if utility < 0:
        print("MIN won the game")
    else:
        print("MAX won the game")
