class Field(object):
    board = []
    def __init__(self):
        for x in range(10):
            self.board.append(["O"] * 10)
    print ("Let's play Battleship!")
    def print_field(self):
        for row in self.board:
            print(" ".join(row))

    def add_ship(self,size, x, y):
        for i in range(size):
            if self.board[x - 1][y + i - 1] == "-":
                print("Sorry. These cells are occupied!")
                return
        for i in range(size):
            if self.board[x - 2][y + i - 2] != "O" or self.board[x - 1][y + i - 2] != "O" \
                    or self.board[x][y + i - 2] != "O" or self.board[x - 2][y + i - 1] != "O" \
                    or self.board[x][y + i - 1] != "O" or self.board[x - 2][y + i] != "O" \
                    or self.board[x - 1][y + i] != "O" or self.board[x][y + i] != "O":
                print("Sorry. Another ship stands near here.")
                return
        for i in range(size):
            self.board[x - 1][y + i - 1] = "-"



    def fire(self, x, y):
        print("Your turn is: "+ str(x) + "," + str(y))
        if self.board[x - 1][y - 1] == "-":
            self.board[x - 1][y - 1] = "X"
            print("Congratulations! You've hit!")
            return True
        else:
            self.board[x - 1][y - 1] = "*"
            print("You missed my battleship!")
            return False

field = Field()
field.add_ship(3, 5, 5)
field.print_field()
print(field.fire(5, 5))
field.print_field()
print(field.fire(1, 1))
field.print_field()
print("Add another ship")
field.add_ship(3, 6, 1)
field.print_field()
