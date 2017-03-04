class Field(object):
    def __init__(self):
        """"It creates a field with the letter O"""
        self.board = []
        for x in range(10):
            self.board.append(["O"] * 10)

    print("Let's play Battleship!")

    def print_field(self):
        """This method prints a field"""
        for row in self.board:
            print(" ".join(row))

    def occupied(self, x, y):
        """The method shows whether a cell is occupied or not"""
        if self.in_field(x, y):
            return self.board[x][y] != "O"
        else:
            return False

    def in_field(self, x, y):
        """"The method shows whether a cell is situated in the borders of field or not"""
        return 0 <= x < 10 and 0 <= y < 10

    def add_ship_horizontal(self, size, x, y):
        """"Add horizontal ships on a field"""
        if size < 5:
            for i in range(size):
                if not self.in_field(x - 1, y + i - 1) or self.board[x - 1][y + i - 1] == "-":
                    print("Sorry. These cells are occupied or out of the field!")
                    return False
                elif self.occupied(x - 2, y + i - 2) or self.occupied(x - 1, y + i - 2) \
                        or self.occupied(x, y + i - 2) or self.occupied(x - 2, y + i - 1) \
                        or self.occupied(x, y + i - 1) or self.occupied(x - 2, y + i) \
                        or self.occupied(x - 1, y + i) or self.occupied(x, y + i):
                    print("Sorry. Another ship stands near here.")
                    return False
            for i in range(size):
                self.board[x - 1][y + i - 1] = "-"
            return True
        else:
            print("The size of the inputted ship is too big. Max size must be 4 cells")
            return False

    def add_ship_vertical(self, size, x, y):
        """"Add vertical ships on a field."""
        if size < 5:
            for i in range(size):
                if not self.in_field(x + i - 1, y - 1) or self.board[x + i - 1][y - 1] == "-":
                    print("Sorry. These cells are occupied or out of the field!")
                    return False
                elif self.occupied(x + i, y - 1) or self.occupied(x + i, y) \
                        or self.occupied(x + i - 1, y) or self.occupied(x + i - 2, y) \
                        or self.occupied(x + i - 2, y - 1) or self.occupied(x + i - 2, y - 2) \
                        or self.occupied(x + i - 1, y - 2) or self.occupied(x + i, y - 2):
                    print("Sorry. Another ship stands near here.")
                    return False
            for i in range(size):
                self.board[x + i - 1][y - 1] = "-"
            return True
        else:
            print("The size of the inputted ship is too big. Max size must be 4 cells")
            return False

    def add_ship(self, size, x, y, direction):
        """"If user inputs h this method calls method add_ship_horizontal otherwise it calls method add_ship_vertical."""
        if direction.lower() == "h":
            return self.add_ship_horizontal(size, x, y)
        elif direction.lower() == "v":
            return self.add_ship_vertical(size, x, y)

    def fire(self, x, y):
        """"It lets to fire at the ship"""
        if self.board[x - 1][y - 1] == "-":
            self.board[x - 1][y - 1] = "X"
            print("Congratulations! You've hit!")
            return True
        else:
            self.board[x - 1][y - 1] = "*"
            print("You missed my ship!")
            return False
