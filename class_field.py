from random import randint


class Field(object):
    board = []
    def __init__(self):
        for x in range(10):
            self.board.append(["O"] * 10)
    print ("Let's play Battleship!")
    def print_field(self):
        for row in self.board:
            print(" ".join(row))

    def add_ship(self, x, y):
        self.board[x][y] = "X"

    def fire(self, x, y):
        if self.board[x][y] == "X":
            return True
        else:
            return False


field = Field()
field.add_ship(5, 5)
field.print_field()
print(field.fire(5, 5))
print(field.fire(1, 1))


