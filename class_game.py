from class_field import *
class Game(object):
     def __init__(self):
         self.players_field = Field()
         self.computers_field = Field()

     def set_players_ships(self):
         for i in range(10):
             self.answer_set_ships = input("Do you want to set ship? ")
             if self.answer_set_ships.lower() == "y":
                 self.answer_set_ships  = input("Please input your coordinates of ship (size x y direction): ")
                 [size, x, y, direction] = self.answer_set_ships.split(" ")
                 self.players_field.add_ship(int(size), int(x), int(y), direction)
                 self.players_field.print_field()
                 print("Your ship was set.")
             else:
                 print("You shoud set your ships if you want to play.")
                 break

     def start(self):
         self.set_players_ships()
         self.answer_start = input("Do you want fire? ")
         if self.answer_start.lower() == "y":
             self.answer_start = input("Please input coordinates of fire (x y): ")
             [x, y] = self.answer_start.split(" ")
             self.players_field.fire(int(x), int(y))
             self.players_field.print_field()
         else:
             print("Come on! Don't you want to play game?")

game = Game()
game.start()