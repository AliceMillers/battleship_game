from class_field import *
import random
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
                print("Your ship was set.")
            elif answer_set_ships.lower() == "n":
                return False
            else:
                print("You shoud set your ships if you want to play.")
                return False
        return True

    def start(self):
        if not self.set_players_ships():
            return
        fire_again_user = True
        fire_again_computer = True
        while fire_again_user:
            answer_start = input("Do you want fire? ")
            if answer_start.lower() == "y":
                answer_start = input("Please input coordinates of fire (x y): ")
                [x, y] = answer_start.split(" ")
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
            if self.players_field.fire(computer_fire_x, computer_fire_y):
                fire_again_computer = True
            else:
                fire_again_computer = False
            self.players_field.print_field()

game = Game()
game.start()