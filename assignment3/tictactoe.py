class TictactoeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class Board:
    valid_moves=["upper left", "upper center", "upper right", "middle left", 
                 "center", "middle right", "lower left", "lower center", 
                 "lower right"]

    def __init__(self):
        self.turn = "X"
        self.board_array = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        pass
    #turn board spaces into a displayable string
    def __str__(self): 
        #self.board_array --> contains " " as a value
        lines=[]
        lines.append(f" {self.board_array[0][0]} | {self.board_array[0][1]} | {self.board_array[0][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[1][0]} | {self.board_array[1][1]} | {self.board_array[1][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[2][0]} | {self.board_array[2][1]} | {self.board_array[2][2]} \n")
        return "".join(lines)

    #Determines if a move is valid or not
    def move(self, move_string):
        #Throws exception if the move is invalid
        if not move_string in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")
        
        move_index = Board.valid_moves.index(move_string)
        row = move_index // 3 # row
        column = move_index % 3 #column
        
        if self.board_array[row][column] != " ":
            raise TictactoeException("That spot is taken.")
        self.board_array[row][column] = self.turn
        #Valid turn add "X" or "O"
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    #Check if the game's over 
    #Creates tuples with each move          
    def whats_next(self):
        #Displays message if game is won or a tie
        cat = True
        for i in range(3):
            for j in range(3):
                if self.board_array[i][j] == " ":
                    cat = False
                else:
                    continue
                break
            else:
                continue
            break
        if (cat):
            return (True, "Cat's Game.")
        win = False
        for i in range(3): # check rows
            if self.board_array[i][0] != " ":
                if self.board_array[i][0] == self.board_array[i][1] and self.board_array[i][1] == self.board_array[i][2]:
                    win = True
                    break
        if not win:
            for i in range(3): # check columns
                if self.board_array[0][i] != " ":
                    if self.board_array[0][i] == self.board_array[1][i] and self.board_array[1][i] == self.board_array[2][i]:
                        win = True
                        break
        if not win:
            if self.board_array[1][1] != " ": # check diagonals
                if self.board_array[0][0] ==  self.board_array[1][1] and self.board_array[2][2] == self.board_array[1][1]:
                    win = True
                if self.board_array[0][2] ==  self.board_array[1][1] and self.board_array[2][0] == self.board_array[1][1]:
                    win = True
        if not win:
            if self.turn == "X": 
                return (False, "X's turn.")
            else:
                return (False, "O's turn.")
        else:
            if self.turn == "O":
                return (True, "X wins!")
            else:
                return (True, "O wins!")

game = Board()
print(game)

#while loop prompt for move, call methods to determine a win or draw
while True:
    try:
        user = input("Make the next move!! ")
        game.move(user)
        print(game)
        #unpacking tuple
        done, message = game.whats_next()
        
        if done:
            print(message)
            break
        
    except Exception as e:
        print(f"An error has occurred: {e}")