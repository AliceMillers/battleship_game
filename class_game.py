from class_field import *
import random
from contextlib import contextmanager
import sys, os

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout

class Game(object):
    def __init__(self):
        self.players_field = Field()
        self.computers_field = Field()

    def set_players_ships(self):
        for i in range(1):
            answer_set_ships = input("Do you want to set ship?(y/n) ")
            if answer_set_ships.lower() == "y":
                answer_set_ships  = input("Please input your coordinates of ship (size x y direction): ")
                [size, x, y, direction] = answer_set_ships.split(" ")
                self.players_field.add_ship(int(size), int(x), int(y), direction)
                self.players_field.print_field()
            elif answer_set_ships.lower() == "n":
                return False
            else:
                print("You shoud set your ships if you want to play.")
                return False
        print("Your ships were set.")
        return True

    def __try_set_computer_ship(self, size):
        ship_ready = False
        while not ship_ready:
            x = random.randint(1, 10)
            y = random.randint(1, 10)
            d = random.randint(0, 2)
            if d < 1:
                direction = "v"
            else:
                direction = "h"
            if self.computers_field.add_ship(size, x, y, direction):
                ship_ready = True

    def set_computers_ships(self):
        ship_sizes = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        for size in ship_sizes:
            self.__try_set_computer_ship(size)
        print("Computers ships were set.")
        self.computers_field.print_field()
        return True

    def start(self):
        if not self.set_players_ships():
            return
        with suppress_stdout():
            if not self.set_computers_ships():
                return
        self.computers_field.print_field()
        print("Computers ships were set.")

        fire_again_user = True
        fire_again_computer = True
        while fire_again_user:
            answer_start = input("Do you want fire?(y/n) ")
            if answer_start.lower() == "y":
                answer_start = input("Please input coordinates of fire (x y): ")
                [x, y] = answer_start.split(" ")
                print("Your turn is: " + str(x) + "," + str(y))
                if self.computers_field.fire(int(x), int(y)):
                    fire_again_user = True
                else:
                    fire_again_user = False
                self.computers_field.print_field()
            else:
                print("Come on! Don't you want to play game?")
                fire_again_user = False
        while fire_again_computer:
            computer_fire_x = random.randint(1, 10)
            computer_fire_y = random.randint(1, 10)
            print("Computer's turn is: " + str(computer_fire_x) + "," + str(computer_fire_y))
            if self.players_field.fire(computer_fire_x, computer_fire_y):
                fire_again_computer = True
            else:
                fire_again_computer = False
            self.players_field.print_field()

game = Game()
game.start()