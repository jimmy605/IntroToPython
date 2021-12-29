import random


# 7.11 - tic tac toe with player against the computer

# Computer needs to check all possible positions it can play, then pick a random index of the avaiable indexes


class TicTactoe:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):
        # Get user input asking if they want to go first or not
        first_player = input('Does the human want to go first (yes or no): ')
        
        return 'X' if first_player in ['yes', 'YES', 'Yes', 'Y', 'y'] else 'O'

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def is_player_win(self, player):
        win = None

        n = len(self.board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'
    
    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=' ')
            print()

    def start(self):
        self.create_board()

        player = self.get_random_first_player()
        if player == 'X':
            print('Human player to go first')
        else:
            print('Computer to go first')
        
        while True:
            print(f'Player {player} turn')

            self.show_board()

            # taking user input
            row, col = list(
                map(int, input('Enter row and column numbers to fix spot: ').split()))

            # fixing the spot
            self.fix_spot(row - 1, col - 1, player)

            # Checking whether current player is won or not
            if self.is_player_win(player):
                print(f'Player {player} wins the game!')
                break

            # Checking whether the game is drawn or not
            if self.is_board_filled():
                print('Match Drawn!!!')
                break

            # swapping the turn
            player = self.swap_player_turn(player)

        # show the final view of the board
        print()
        self.show_board()


# starting the game
tic_tac_toe = TicTactoe()
tic_tac_toe.start()
