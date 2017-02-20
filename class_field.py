class Field(object):
    def __init__(self):
        self.board = []
        for x in range(10):
            self.board.append(["O"] * 10)
    print ("Let's play Battleship!")
    def print_field(self):
        for row in self.board:
            print(" ".join(row))

    def occupied(self, x, y):
        if self.in_field(x, y):
            return self.board[x][y] != "O"
        else:
            return False

    def in_field(self, x, y):
        return 0 <= x < 10 and 0 <= y < 10

    def add_ship_horizontal(self,size, x, y):
        if size < 5:
            for i in range(size):
                if not self.in_field(x - 1,  y + i - 1) or self.board[x - 1][y + i - 1] == "-":
                    print("Sorry. These cells are occupied or out of the field!")
                    return
                elif self.occupied(x -2, y + i -2) or self.occupied(x - 1, y + i - 2) \
                        or self.occupied(x, y + i - 2) or self.occupied(x - 2, y + i - 1) \
                        or self.occupied(x, y + i - 1) or self.occupied(x - 2, y + i) \
                        or self.occupied(x - 1, y + i) or self.occupied(x, y + i):
                    print("Sorry. Another ship stands near here.")
                    return
            for i in range(size):
                self.board[x - 1][y + i - 1] = "-"
        else:
            print("The size of the inputted ship is too big. Max size must be 4 cells")

    def add_ship_vertical(self,size, x, y):
        if size < 5:
            for i in range(size):
                if not self.in_field(x + i - 1, y - 1) or self.board[x + i - 1][y - 1] == "-":
                    print("Sorry. These cells are occupied or out of the field!")
                    return
                elif self.occupied(x + i, y - 1) or self.occupied(x + i, y) \
                        or self.occupied(x + i - 1, y) or self.occupied(x + i - 2, y) \
                        or self.occupied(x + i - 2, y - 1) or self.occupied(x + i - 2, y - 2) \
                        or self.occupied(x + i - 1, y - 2) or self.occupied(x + i, y - 2):
                    print("Sorry. Another ship stands near here.")
                    return
            for i in range(size):
                self.board[x + i - 1][y - 1] = "-"
        else:
            print("The size of the inputted ship is too big. Max size must be 4 cells")

    def add_ship(self, size, x, y, direction):
        if direction.lower() == "h":
            self.add_ship_horizontal(size, x, y)
        elif direction.lower() == "v":
            self.add_ship_vertical(size, x, y)

    def fire(self, x, y):
        if self.board[x - 1][y - 1] == "-":
            self.board[x - 1][y - 1] = "X"
            print("Congratulations! You've hit!")
            return True
        else:
            self.board[x - 1][y - 1] = "*"
            print("You missed my battleship!")
            return False

field = Field()
#field.add_ship_horizontal(3, 5, 5)
#field.add_ship_vertical(2, 2, 2)
#field.print_field()
#print(field.fire(5, 5))
#field.print_field()
#print(field.fire(1, 1))
#field.print_field()
#field.add_ship_horizontal(3, 7, 1)
#field.add_ship_vertical(4, 1, 3)
#field.print_field()
