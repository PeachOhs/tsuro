"""
A board of tiles for the Tsuro game.

:Author:     Matthew Goczalk
:Version:    v1.0
"""

from helper import *

class TileBoard:
    """
    A TileBoard is a representation of the Tsuro board as a graph.
    An R*C board in the game is represented by a grid graph with
    R rows and C columns. The R*C board will be referred to as
    the tile board.
    """

    def __init__(self, rows, cols):
        """
        Creates a new TileBoard.

        Args:
            rows (int): Number of rows in the board.
            cols (int): Number of columns in the board.
        """
        self.rows = rows
        self.cols = cols
        self.graph_rows = 3 * rows + 1
        self.graph_cols = 3 * cols + 1
        self.board = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        self.dragon_tile_locations = None

    def add_tile(self, tile, board_index):
        """
        Adds a tile to the board.

        Args:
            tile (Tile): Tile to add to the board.
            board_index (tuple): Row and column index of the tile in the 
                tile board.
        """
        try:
            if tile.is_dragon_tile:
                self.dragon_tile_locations = []
                self.dragon_tile_locations.append(board_index)
                return
            else:
                self.board[board_index[0]][board_index[1]] = tile
        except:
            self.board[board_index[0]][board_index[1]] = tile
