from board import Board
from player import *
from numpy import random
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
        random.shuffle(playerNames)
        for p in range(num_players):
            playerA = Player(playerNames[p], p)
            self.add_player(playerA, p)
            self.active_player(playerA, p)
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

    def active_player(self, player, turn):
        """
        Adds a player to the game.

        Args:
            player (Player): Player to add to game.
            turn (int): Player's turn, zero-indexed.
        """
        self.active_players[turn] = player

    def start(self):
        """
        Starts the game.
        """
        if all([x is not None for x in self.players]):
            self.in_game = True
        #if self.in_game == True:
            self.next_turn()

    def add_tile(self, tile, board_index):
        """
        Adds a tile to the board.

        Args:
            tile (Tile): Tile to add to the board.
            board_index (tuple): Row and column index of the tile in the 
                tile board.
        """
        self.board.add_tile(tile, board_index)

    def move(self):
        """
        Moves the current player along the line.
        """
        if not self.board.move(self.current_player):
            self.players[self.current_player.turn] = None

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
                print("Inactive: "+player.get_name())
        print(str(countActive)+"/"+str(self.num_players))
        self.active_players = [None] * countActive
        for p in activeOrder:
            self.active_player(self.players[p], p)
            #print("Active: "+self.players[p].get_name())
        if countInactive >= self.num_players-1:
            self.in_game = False
            return
        while True:
            #self.current_player = self.players
            """
            cycle through self.players
            """
            if self.current_player is not None:
                idx = -1
                try:
                    idx = self.active_players.index(self.current_player)
                except:
                    pass
                if idx > -1:
                    self.current_player = self.active_players[idx+1]
                    print("Current player: "+self.current_player.get_name())
                    break
                idx = self.players.index(self.current_player)
                """while True:
                    print("Current player: "+self.current_player)
                    break"""
            else:
                self.current_player = self.players[0]
                print("Current player: "+self.current_player.get_name())
                break

    def winner(self):
        """
        Returns the winner of the game.
        """
        if not self.in_game:
            for player in self.players:
                if player is not None:
                    count += 1
                    print("Winner: "+player.get_name())
