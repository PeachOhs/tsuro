"""
A player for the Tsuro game.

:Author:     Maded Batara III
:Version:    v1.0
"""

class Player:
    """
    The Player class is a helper class for the Tsuro player.
    """

    def __init__(self, name, turn):
        """
        Creates a new Player.

        Args:
            name (str): Name of player.
            turn (int): Zero-based index indicating player turn.
        """
        self.name = name
        self.player = Player
        self.turn = turn
        self.hand = []
        self.visited = []
        self.in_game = False
        self.index = 0

    def __iter__(self):
        # Returns the iterator object (in this case, self)
        return self
    
    def __next__(self):
        # Provides the next item in the sequence
        if self.index < len(self.name):
            item = self.name[self.index]
            self.index += 1
            return item
        else:
            # Raises StopIteration when no more items are available
            raise StopIteration

    def add_to_visited(self, graph_index):
        """
        Adds a graph node to the list of visited nodes.

        Args:
            graph_index (tuple): Row and column index of node to add.
        """
        self.visited.append(graph_index)

    def add_to_hand(self, tile):
        """
        Adds a tile to the Player's hand.

        Args:
            tile (Tile): Tile to add to hand.
        """
        self.hand.append(tile)

    def get_from_hand(self):
        """
        Gets a tile from the Player's hand.
        """
        return self.hand.pop()

    def get_name(self):
        return str(self.name)
