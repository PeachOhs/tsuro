from game import *
from deck import *

Deck = Deck()
Game = Game(8, Deck, 6, 6)
Game.start()

print("Reached end of main.py")
