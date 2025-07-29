"""
A deck of tiles for the Tsuro game.

:Author:     Maded Batara III
:Version:    v1.0
"""

import json
from numpy import random
from tile import *
import numpy as np

class Deck:
    """
    The Deck class is a helper class containing a list of tiles.
    """

    def __init__(self):
        """
        Creates a new Deck.
        """
        self.deck = []
        with open('tiles.json') as json_file:
            data = json.load(json_file)
        a = np.arange(1,36)
        random.shuffle(a)

        for i in range(35):
            connected_pairs = []
            found_values = []
            positions = [0,1,2,3,4,5,6,7]
            for p in positions:
                if not p in found_values:
                    connected_pairs.append((p,int(data[a[i]][str(p)])))
                    found_values.append(int(data[a[i]][str(p)]))
            tile = Tile(data[a[i]]["tile"], connected_pairs)
            self.push(tile)
        
        self.shuffle()
        connected_pairs = []
        tile = Tile(data[a[0]]["tile"], connected_pairs)
        tile.is_dragon_tile = True
        self.push(tile)

    def push(self, tile):
        """
        Adds a tile to the deck. Occurs when a player is eliminated.

        Args:
            tile (Tile): Tile to add to the deck.
        """
        self.deck.append(tile)

    def pop(self):
        """
        Gets and returns a tile from the deck.
        """
        return self.deck.pop()

    def shuffle(self):
        from random import shuffle
        shuffle(self.deck)