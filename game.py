from board import Board
from player import *
from numpy import random
from helper import *
import numpy
import array
import itertools

"""
A wrapper for the Tsuro game.

:Author:     Maded Batara III
:Version:    v1.0
"""

class Game:
    """
    The Game class wraps around all the classes in the Tsuro module.
    """

    def __init__(self, num_players, deck, rows, cols):
        """
        Creates a new Game.

        Args:
            num_players (int): Number of players in the game.
            deck (Deck): Deck containing cards.
            rows (int): Number of rows in the board.
            cols (int): Number of columns in the game.
        """
        self.num_players = num_players
        self.deck = deck
        self.board = Board(rows, cols)
        self.players = [None] * num_players
        self.active_players = [None] * num_players
        #self.players = []
        playerNames = ["Red","Orange","Yellow","Green","Blue","Indigo","Violet","White"]
        #random.shuffle(playerNames)
        for p in range(num_players):
            playerA = Player(playerNames[p], p)
            self.add_player(playerA, p)
            self.active_player(playerA)
            #self.players.append(playerA)
        self.in_game = False
        self.current_player = None

    def add_player(self, player, turn):
        """
        Adds a player to the game.

        Args:
            player (Player): Player to add to game.
            turn (int): Player's turn, zero-indexed.
        """
        player.add_to_game()
        self.players[turn] = player

    def active_player(self, player):
        """
        Adds a player to the game.

        Args:
            player (Player): Player to add to game.
            turn (int): Player's turn, zero-indexed.
        """
        # set player to first None in self.active_players
        self.active_players[self.active_players.index(None)] = player

    def start(self):
        """
        Starts the game.
        """
        if all([x is not None for x in self.players]):
            self.in_game = True
        
        i = 0
        # activate below line once full game logic is in place
        #while (self.in_game):
        # deactivate below line once full game logic is in place
        while (i in numpy.arange(0,32) and self.in_game) and self.in_game and self.current_player != None:
            self.next_turn()
            #TODO: Facing should be A, B, C, D, -A, -B, -C, or -D
            current_graph_position = self.board.player_board.current_position(self.current_player)
            print(current_graph_position)
            facing = get_facing(current_graph_position,self.board.tile_board)
            print(facing)
            # test place tiles
            tilePlace = board_index_to_tile_side(current_graph_position, self.board.graph_rows, self.board.graph_cols, ("-"+str(facing)))
            print(tilePlace)
            self.add_tile(self.current_player.get_from_hand(),tilePlace)
            # test eliminate player on their turn
            if i in numpy.array([10,13,18,24]):
                self.current_player.remove_from_game()
            # test eliminate player on another player's turn
            if i in numpy.array([14,18,22]):
                self.active_players[0].remove_from_game()
            # deactivate below line once full game logic is in place
            i += 1

    def add_tile(self, tile, board_index):
        """
        Adds a tile to the board.

        Args:
            tile (Tile): Tile to add to the board.
            board_index (tuple): Row and column index of the tile in the 
                tile board.
        """
        tile.transform()
        self.board.add_tile(tile, board_index)

        tile_indexes = []
        for i in numpy.arange(0,8):
            tile_indexes.append(tile_to_board_index(i,board_index))

        # Move current player
        self.move(self.current_player)
        # Move every other player if they were on tilePlace
        for moving_player in self.active_players:
            if moving_player != self.current_player and moving_player.visited[-1] in tile_indexes:
                self.move(moving_player)

    def move(self, player):
        """
        Moves the current player along the line.
        """
        if not self.board.move(player):
            #self.players[player.turn] = None
            player.remove_from_game()
        if on_edge(player.visited[-1], self.board.player_board.graph_rows, self.board.player_board.graph_cols):
            player.remove_from_game()

    def next_turn(self):
        """
        Moves the game to the next player/turn.
        """
        countActive = 0
        countInactive = 0
        #activeOrder = []
        activeOrder = array_of_signed_ints = array.array("i")
        for player in self.players:
            if player is not None and player.in_game:
                countActive += 1
                #print("Active: "+player.get_name())
                #active += player
                activeOrder.append(self.players.index(player))
                #activeOrder += int(self.players.index(player))
            else:
            #elif player.in_game == False:
                countInactive += 1
                #print("Inactive: "+player.get_name())
        #print(str(countActive)+"/"+str(self.num_players))
        self.active_players = [None] * countActive
        for p in activeOrder:
            self.active_player(self.players[p])
            #print("Active: "+self.players[p].get_name())
        if countInactive >= self.num_players-1:
            self.in_game = False
            self.winner()
            return
        while True:
            #self.current_player = self.players
            """
            cycle through self.players
            """
            if self.current_player is not None:
                idx = None
                try:
                    idx = self.active_players.index(self.current_player)
                except:
                    # current_player is no longer active
                    idx = self.players.index(self.current_player)
                    # set idx to the first active player just before the current_player
                    while True:
                        idx -= 1
                        if idx < 0:
                            idx += self.num_players
                        if self.players[idx] in self.active_players:
                            idx = self.active_players.index(self.players[idx])
                            break
                    pass
                idx += 1
                if idx >= (countActive):
                    idx = idx - countActive
                if idx is not None:
                    self.current_player = self.active_players[idx]
                    print("Current player: "+self.current_player.get_name())
                    break
                idx = self.players.index(self.current_player)
                """while True:
                    print("Current player: "+self.current_player)
                    break"""
            else:
                # draw 3 tiles per player
                for three in numpy.arange(0,3):
                    for drawplayer in self.players:
                        if drawplayer is not None:
                            tile = self.deck.pop()
                            drawplayer.add_to_hand(tile)
                            if three == 2:
                                # Place player pawn on edge of board
                                #print("Place "+ drawplayer.get_name() +" pawn on edge of board")
                                self.board.player_board.place(drawplayer,self.board.edge_nodes.pop())
                    three += 1
                self.current_player = self.players[0]
                print("First player: "+self.current_player.get_name())
                break

    def winner(self):
        """
        Returns the winner of the game.
        """
        if not self.in_game:
            for player in self.active_players:
                if player is not None:
                    #count += 1
                    print("Winner: "+player.get_name())
