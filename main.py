from game import *
from deck import *

Deck = Deck()
Game = Game(8, Deck, 6, 6)
Game.start()
print(Game.players)
Game.next_turn()
Game.next_turn()
Game.next_turn()
Game.next_turn()
Game.next_turn()
Game.next_turn()
Game.next_turn()
print("End main.py")
