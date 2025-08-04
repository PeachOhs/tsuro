from game import *
from deck import *

Deck = Deck()
Game = Game(8, Deck, 6, 6)
Game.start()
print(Game.players)

print("End main.py")
