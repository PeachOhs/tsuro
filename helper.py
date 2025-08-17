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
    
    if tile_index <= 1:
        row_offset = 0
    elif tile_index in [7, 2]:
        row_offset = 1
    elif tile_index in [6, 3]:
        row_offset = 2
    else:
        row_offset = 3
    
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

def board_index_to_tile(graph_index, tile_index):
    """
    Converts an (x, y) graph board index to a board index.

    Args:
        graph_index (tuple): Row and column index of the position in the 
            graph board.
        tile_index (int): Index of node in tile.
    Returns:
        A 2-tuple indicating the tile's position in the board.
    """

    if tile_index <= 1:
        row_offset = 0
    elif tile_index in [7, 2]:
        row_offset = 1
    elif tile_index in [6, 3]:
        row_offset = 2
    else:
        row_offset = 3
    
    if tile_index > 5:
        column_offset = 0
    elif 1 < tile_index < 4:
        column_offset = 3
    elif tile_index in [0, 5]:
        column_offset = 1
    else:
        column_offset = 2
    return (int((graph_index[0] - column_offset)/3),int((graph_index[1] - row_offset)/3))

def board_index_to_tile_side(graph_index, side, rows, cols):
    """
    Converts an (x, y) graph board index to a board index.

    Args:
        graph_index (tuple): Row and column index of the position in the 
            graph board.
        facing (str/int): Index of the tile facing, with a negative value going to the opposing tile sharing the graph_index.
        rows (int): Number of rows in the grid graph.
        cols (int): Number of columns in the grid graph.
    Returns:
        A 2-tuple indicating the tile's position in the board.
    """

    row_offset = 0
    column_offset = 0

    if side is None:
        if on_edge(graph_index, rows, cols):
            # set side based on edge
            if graph_index[0] == 0:
                side = "D"
            elif graph_index[0] == rows - 1:
                side = "B"
            elif graph_index[1] == 0:
                side = "A"
            elif graph_index[1] == cols - 1:
                side = "C"
        else:
            raise Exception("For board_index_to_tile_side, side is needed when graph_index not on edge")

    if side == "B" or side == 2 or side == -4 or side == "-D":
        tile_index = graph_index[1]%3 + 1
        if str(side)[0] == "-":
            column_offset = 1
        #tile_index = 2
        #tile_index = 3
    elif side == "C" or side == 3 or side == -1 or side == "-A":
        tile_index = abs(graph_index[0]%3 - 6)
        if str(side)[0] == "-":
            row_offset = 1
        #tile_index = 4
        #tile_index = 5
    elif side == "D" or side == 4 or side == -2 or side == "-B":
        tile_index = abs(graph_index[1]%3 - 8)
        if str(side)[0] == "-":
            column_offset = -1
        #tile_index = 6
        #tile_index = 7
    else:#if side == "A" or side = 1 or side == -3 or side == "-C":
        tile_index = graph_index[0]%3 - 1
        if str(side)[0] == "-":
            row_offset = -1
        #tile_index = 0
        #tile_index = 1

    board_index = board_index_to_tile(graph_index, int(tile_index))
    #print("("+str(graph_index[0])+", "+str(graph_index[1])+"), "+str(tile_index)+" => ("+str(board_index[0])+", "+str(board_index[1])+")")
    return (int(board_index[0] + column_offset),int(board_index[1] + row_offset))

def board_index_to_tile_pair(graph_index, rows, cols):
    """
    Converts an (x, y) graph board index to one or two board indexes.

    Args:
        graph_index (tuple): Row and column index of the position in the 
            graph board.
        rows (int): Number of rows in the grid graph.
        cols (int): Number of columns in the grid graph.
    Returns:
        A list of 2-tuple(s) indicating the tile's position(s) in the board.
    """
    tiles = []

    """
    graph_index[0] = col
    graph_index[1] = row
    """

    if (graph_index[0]%3 in [1,2] and graph_index[1]%3 in [0,3]) or (graph_index[1]%3 in [1,2] and graph_index[0]%3 in [0,3]):
        if graph_index[0] == 0:
            facings = ["-D"] # facing right
        elif graph_index[1] == 0:
            facings = ["-A"] # facing down
        elif graph_index[0] == cols - 1:
            facings = ["-B"] # facing left
        elif graph_index[1] == rows - 1:
            facings = ["-C"] # facing up
        elif graph_index[0]%3 in [1,2]:
            facings = ["-C","-A"] # facing up or down
        elif graph_index[1]%3 in [1,2]:
            facings = ["-D","-B"] # facing left or right
    else:
        raise Exception("illegal graph_index: ("+str(graph_index[0])+", "+str(graph_index[1])+")")

    for facing in facings:
        row_offset = 0
        column_offset = 0
        if facing == "B" or facing == 2 or facing == -4 or facing == "-D":
            tile_index = graph_index[1]%3 + 1
            if str(facing)[0] == "-":
                column_offset = 1
            #tile_index = 2
            #tile_index = 3
        elif facing == "C" or facing == 3 or facing == -1 or facing == "-A":
            tile_index = abs(graph_index[0]%3 - 6)
            if str(facing)[0] == "-":
                row_offset = 1
            #tile_index = 4
            #tile_index = 5
        elif facing == "D" or facing == 4 or facing == -2 or facing == "-B":
            tile_index = abs(graph_index[1]%3 - 8)
            if str(facing)[0] == "-":
                column_offset = -1
            #tile_index = 6
            #tile_index = 7
        else:#if facing == "A" or facing = 1 or facing == -3 or facing == "-C":
            tile_index = graph_index[0]%3 - 1
            if str(facing)[0] == "-":
                row_offset = -1
            #tile_index = 0
            #tile_index = 1
        board_index = board_index_to_tile(graph_index, tile_index)
        #print("( "+str(board_index[0])+" + "+str(column_offset)+" , "+str(board_index[1])+" + "+str(row_offset)+" )")
        tiles.append((board_index[0] + column_offset,board_index[1] + row_offset))
    return sorted(tiles, key=lambda coord: (coord[0],coord[1]))

def get_facing(graph_index, tile_board):
    """
    Return direction of empty tile.

    Args:
        graph_index (tuple): Row and column index of the position in the 
            graph board.
        tile_board: Positions of the tiles on the board
    Returns:
        An int indicating the player's facing direction on the board.
    """
    rows = tile_board.graph_rows
    cols = tile_board.graph_cols
    tile_options = board_index_to_tile_pair(graph_index, rows, cols)

    if graph_index[0] == 0:
        facing = "D" # facing right
    elif graph_index[1] == 0:
        facing = "A" # facing down
    elif graph_index[0]%3 in [1,2]:
        # facing up or down
        for tile_option in tile_options:
            if tile_board[tile_option[0]][tile_option[1]] == None:
                print(str(tile_option[0])+","+str(tile_option[1]))
        facing = ""
    elif graph_index[1]%3 in [1,2]:
        # facing left or right
        for tile_option in tile_options:
            if tile_board[tile_option[0]][tile_option[1]] == None:
                print(str(tile_option[0])+","+str(tile_option[1]))
        facing = ""

    