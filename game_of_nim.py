from games import *

class GameOfNim(Game):

    def __init__(self, board=None):
        if board is None:
            board = [7, 5, 3, 1]
        
        # Calculate and set the init moves
        init_moves = []
        for row in range(len(board)):
            for num_objects in range(1, board[row] + 1):
                init_moves.append((row, num_objects))
                
        # Create the initial state with the calculated moves
        self.initial = GameState(to_move='MAXIMUM', 
                               utility=0, 
                               board=board, 
                               moves=init_moves)

    def actions(self, state):
        moves = []
        for row in range(len(state.board)):
            for num_objects in range(1, state.board[row] + 1):
                moves.append((row, num_objects))
        return moves

    def result(self, state, move):
        board = state.board.copy()
        row, num_objects = move

        # Validate the move
        if row < 0 or row >= len(board) or num_objects > board[row]:
            return state
        
        # Applies the move
        board[row] -= num_objects

        # Calculate next player
        next_player = 'MINIMUM' if state.to_move == 'MAXIMUM' else 'MAXIMUM'

        # Calculate utility
        utility = 0
        if sum(board) == 0:
            utility = 1 if next_player == 'MAXIMUM' else -1

        # Calculate new valid moves
        # Generates the new valid moves based on the updated board
        new_moves = [(row, num_objects) for row in range(len(board)) for num_objects in range(1, board[row] + 1)]
        return GameState(to_move=next_player,
                        utility=utility,
                        board=board,
                        moves=new_moves)

    def utility(self, state, player):
        # Return the value to player; 1 for win, -1 for loss, 0 otherwise.
        return 1 if state.utility == 1 and player == 'MAXIMUM' else -1 if state.utility == -1 and player == 'MINIMUM' else 0

    def terminal_test(self, state):
        
        return sum(state.board) == 0

    def display(self, state):
        board = state.board
        print("board: ", board)


if __name__ == "__main__":
    nim = GameOfNim(board=[7, 5, 3, 1]) # a much larger search
    result_state = nim.result(nim.initial, (1,2)) # the computer moves first
    print(nim.initial.board)
    print(nim.initial.moves) 
    print(nim.result(nim.initial, (1,3)).board)
    utility = nim.play_game(alpha_beta_player, query_player) # the computer moves first 
    if utility == -1:
        print("MINIMUM won the game")
    else:
        print("MAXIMUM won the game")