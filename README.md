# Tsuro

A Python module for the Tsuro game. Includes models for each game element and a sample Game wrapper.

## Objectives

The primary objective of this python repository is to make a functional game of [Tsuro: The game of the Path.](https://boardgamegeek.com/boardgame/16992/tsuro) The secondary objective of this python repository is to use either [wave-function collapse](https://github.com/Coac/wave-function-collapse) or [NEAT (NeuroEvolution of Augmenting Topologies)](https://en.wikipedia.org/wiki/Neuroevolution_of_augmenting_topologies) à la [Code Bullet](https://www.youtube.com/@CodeBullet) to find end-game board-state(s) that involve all players winning the game.

## TODO
- [x] [main.py](main.py) launches the game and builds the deck
- [x] [deck.py](deck.py) initializes the deck
    - [x] add the tiles in the deck
    - [x] remove the tiles in the deck
    - [x] shuffle the tiles in the deck
- [x] [game.py](game.py) initializes the players and deck
    - [ ] each player draws 3 tiles
    - [ ] each player places their pawn on one of the outside marks on the board
    - [x] starts the first and subsequent turns
    - [ ] player turn functionality
        - [ ] current player places a path tile
        - [ ] current player moves all pawns along the paths on the path tile played
            - [ ] if a player pawn moves off the board or collides with another player pawn, they are eliminated
                - [ ] that player returns their tiles to the deck
                - [ ] any player with the dragon tile draws from the deck and passes the dragon tile to the next player
                - [ ] once all players have 3 tiles, the dragon tile returns to the deck
        - [ ] current player draws a new path tile from the deck if tiles are in the deck
- [ ] UI for the game

## Passed Testing
