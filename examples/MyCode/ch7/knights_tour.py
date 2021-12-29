"""knights_tour.py"""
import numpy as np 


class Knight:
    def __init__(self):
        # Create a 2 dimension board 8 x 8 with all values set to 0
        self.board = np.zeros((8, 8),dtype=str)
        self.position_tracker = [] # Tracker for 1 - 64 squares on the board
        self.current_position = 0 # Position 1 - 64
    
    
    def position_to_index(self, position):
        """Takes a position 1 - 64 and returns a tuple of indices for the 8x8 board"""
        row = position // 8  # Board row
        column = position % 8  # Column
        
        if column == 0:
            return (row - 1, column + 7)
        return (row, column - 1)
    
    
    def game_board(self, position=29):
        """Create the 8 x 8 board and print the starting position of the knight piece when the board is returned"""
        # Add position to the tracker
        self.position_tracker.append(position)
        self.current_position = position
        p = self.position_to_index(position)
        
        self.board[p[0]][p[1]] = 'K' 
        
        return self.board 
    
    
    def move_number(self):
        """Take in the current position of the knight, workout all possible moves and not possible moves"""
        # Current row/column
        current_row = self.position_to_index(self.current_position)[0]
        current_column = self.position_to_index(self.current_position)[1]
        
        # Possible moves. move_num: [horizontal, vertical]
        moves = {0: [2, -1], 1: [1, -2], 2: [-1, -2], 3: [-2, -1], 4: [-2, 1],5: [-1, 2], 6: [1, 2], 7: [2, 1]}
        
        # Need something to check if the horizontal/vertical indexes will work or not
        # Iterate through the moves dict and if the current position can take the horizontal/vertical positions return the possible positions available to move
        # Create another dict to store the passed positions
    
    
    def check_move(self, current_position):
        """Take in the current position and check if the current position of the knight can be moved to one of the eight possible moves the knight can complete"""
        # Possible moves. move_num: [horizontal, vertical]
        moves = {0: [2, -1], 1: [1, -2], 2: [-1, -2], 3: [-2, -1],
                 4: [-2, 1], 5: [-1, 2], 6: [1, 2], 7: [2, 1]}
        
        # append the move number (key) in moves if it's a possible move
        possible_moves = []
        
        for move, col_row in moves.items():
            # Need 4 checks [+, +][+, -], [- , -], [-, +] to factor in each case
            # [+, +]
            if (col_row[0] > 0 and col_row[1] > 0) and (current_position[0] + col_row[0]) <= 7 and (current_position[1] + col_row[1]) <= 7:
                possible_moves.append(move)
        
        return possible_moves


    # Need to check if the knight has been to the position and it's a valid position

game_1 = Knight()
# print(game_1.position_to_index(24))
print(game_1.game_board())
move = game_1.position_to_index(29)
print(game_1.check_move(move))