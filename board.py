from helper import *
from pathboard import PathBoard
from playerboard import PlayerBoard
from numpy import random
import numpy

"""
A board for the Tsuro game.

:Author:     Maded Batara III
:Version:    v1.0

Board: Rows x Cols
xxxxxx
xxxxxx
xxxxxx
xxxxxx
xxxxxx
xxxxxx

Graph Nodes: 3*Rows+1 x 3*Cols+1
 xx xx xx xx xx xx 
x  x  x  x  x  x  x
x  x  x  x  x  x  x
 xx xx xx xx xx xx 
x  x  x  x  x  x  x
x  x  x  x  x  x  x
 xx xx xx xx xx xx 
x  x  x  x  x  x  x
x  x  x  x  x  x  x
 xx xx xx xx xx xx 
x  x  x  x  x  x  x
x  x  x  x  x  x  x
 xx xx xx xx xx xx 
x  x  x  x  x  x  x
x  x  x  x  x  x  x
 xx xx xx xx xx xx 
x  x  x  x  x  x  x
x  x  x  x  x  x  x
 xx xx xx xx xx xx 
"""

class Board:
    """
    The Board class wraps around the PathBoard and PlayerBoard classes,
    allowing them to interact with each other.
    """

    def __init__(self, rows, cols):
        """
        Creates a Board.

        Args:
            rows (int): Number of rows in the board.
            cols (int): Number of columns in the board.
        """
        self.rows = rows
        self.cols = cols
        self.graph_rows = 3 * rows + 1
        self.graph_cols = 3 * cols + 1
        self.path_board = PathBoard(rows, cols)
        self.player_board = PlayerBoard(rows, cols)
        self.edge_nodes = []
        for r in numpy.arange(0,rows):
            for c in numpy.arange(0,cols):
                for i in numpy.arange(0,8):
                    if on_edge(tile_to_board_index(i,(r,c)),self.graph_rows,self.graph_cols):
                        self.edge_nodes.append(tile_to_board_index(int(i),(int(r),int(c))))
        self.edge_nodes = list(set(self.edge_nodes))
        random.shuffle(self.edge_nodes)
        #print("Edge nodes: "+str(len(self.edge_nodes))+" but this needs to be 48")

    def add_tile(self, tile, board_index):
        """
        Adds a tile to the board.

        Args:
            tile (Tile): Tile to add to the board.
            board_index (tuple): Row and column index of the tile in the 
                tile board.
        """
        self.path_board.add_tile(tile, board_index)
        #TODO: self.player_board.move()

    def move(self, player):
        """
        Moves a player along the board.

        Args:
            player (Player): Player to move.

        Returns:
            False if player was removed from game, True otherwise.
        """
        current_position = self.player_board.current_position(player)
        while True:
            adj = self.path_board.adj(current_position)
            if len(adj) == 0:
                break
            current_position = adj[0]
            player.add_to_visited(current_position)
        if current_position in self.path_board.dragon_tile_locations or on_edge(current_position, self.graph_rows, self.graph_cols): 
            self.player_board.remove(player)
            player.in_game = False
            return False
        else:
            self.player_board.move(self, player, current_position)
            return True
