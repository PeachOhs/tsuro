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
    - [x] each player draws 3 tiles
    - [x] each player places their pawn on one of the outside marks on the board
    - [x] starts the first and subsequent turns
    - [ ] player turn functionality
        - [ ] current player places a path tile from the tiles in their hand
            - [ ] if all tiles are on the board, the game ends
        - [ ] current player moves all pawns forward along the paths on the path tile played
            - [ ] if a player pawn moves off the board or collides with another player pawn, they are eliminated
                - [ ] that player returns their tiles to the deck
                    - [ ] if one of their tiles was the dragon tile, it goes to the next player with less than 3 tiles in their hand
                - [ ] any player with the dragon tile draws one tile from the deck and passes the dragon tile to the next player who has less than 3 tiles in their hand
                    - [ ] if all players have 3 tiles, the dragon tile returns to the deck
                - [x] if only 1 player remains, the game ends
        - [ ] current player draws a new path tile from the deck if tiles are in the deck
- [ ] Output board state at the end of the game
- [ ] \(Optional) UI for the game
- [ ] [NEAT implementation](https://neat-python.readthedocs.io/en/latest/)

## Passed Testing
