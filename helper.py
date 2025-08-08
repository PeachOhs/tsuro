"""
Helper functions for the Tsuro game.

:Author:     Maded Batara III
:Version:    v1.0
"""

def tile_to_board_index(tile_index, board_index):
    """
    Converts a 0-7 tile node index to an (x, y) graph board index.

    Args:
        tile_index (int): Index of node in tile.
        board_index (tuple): Row and column index of the tile in the 
            tile board.
    Returns:
        A 2-tuple indicating the node's position in the graph board.
    """
    #row_offset=IF(B23<=1,0,IF(OR(B23=7,B23=2),1,IF(OR(B23=6,B23=3),2,3)))
    if tile_index <= 1:
        row_offset = 0
    elif tile_index in [7, 2]:
        row_offset = 1
    elif tile_index in [6, 3]:
        row_offset = 2
    else:
        row_offset = 3
    #column_offset=IF(B23>5,0,IF(AND(B23>1,B23<4),3,IF(OR(B23=0,B23=5),1,2)))
    if tile_index > 5:
        column_offset = 0
    elif 1 < tile_index < 4:
        column_offset = 3
    elif tile_index in [0, 5]:
        column_offset = 1
    else:
        column_offset = 2
    return (board_index[0] * 3 + column_offset, board_index[1] * 3 + row_offset)

def on_edge(graph_index, rows, cols):
    """
    Checks if the index is at the edge of the board.

    Args:
        graph_index (tuple): Index of node in the graph.
        rows (int): Number of rows in the grid graph.
        cols (int): Number of columns in the grid graph.
    """
    return graph_index[0] == 0 or graph_index[0] == rows - 1 or graph_index[1] == 0 or graph_index[1] == cols - 1