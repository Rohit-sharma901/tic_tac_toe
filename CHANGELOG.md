# Changelog

## [0.8.0] - Exception tests added
### Added
 Unit tests for:
  Invalid move on occupied cell raises `InvalidMoveError`
  Out-of-bounds move raises `InvalidMoveError`

## [0.7.0] - Exception handling added
### Added
`InvalidMoveError` and `GameOverError` custom exceptions
Used `InvalidMoveError` in Board and handled in Game loop

## [0.6.0] - Basic board tests implemented
### Added
Unit tests for board:
   Empty state
   Valid/invalid moves
   Win detection
   Draw detection

## [0.5.0] - Main entry point implemented
### Added
 `main.py` to start the game
 Game start logic (player names input)

## [0.4.0] - Game class implemented
### Added
 `Game` class with:
   Game flow control
   Player turn alternation
   Winner and draw check

## [0.3.0] - Player class implemented
### Added
 `Player` class with:
   Name and symbol attributes
   Move input method with validation

## [0.2.0] - Board class implemented
### Added
 `Board` class with:
   grid initialization
   move validation
   winner check
   draw check
   display method

## [0.1.0] - Initial Setup
### Added
 Project structure
 Game, tests, and core files