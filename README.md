# TIC-TAC-TOE
King AbdulAziz Universality - Computer Graphics (CPCS-391)

## Overview

This project delivers an enhanced version of the classic game Tic-Tac-Toe, developed to challenge players' strategic thinking and offer extended gameplay features. Using Pygame for window management and OpenGL for graphics rendering, this version introduces new dynamics to the traditional Tic-Tac-Toe gameplay.

## Features

- **Extended Gameplay:** Play continues until one player wins, promoting deeper strategic planning.
- **Dynamic Board:** The game board allows only three consecutive symbols; adding a fourth symbol removes the first, continually altering the state of play.
- **Strategic Depth:** Encourages players to think several moves ahead to outmaneuver their opponent.

## Game Mechanics

- **Game Board:** Utilizes a 3x3 grid where players place their marks (X or O).
- **Winning Conditions:** Players aim to align three of their marks horizontally, vertically, or diagonally.
- **Innovative Marker Management:** Introducing mechanics where additional markers can replace the earliest placed markers, refreshing the gameplay dynamics.

## Installation Requirements

To run this application, you must install:
- **Python**: Ensure Python is installed on your machine.
- **Pygame**: Needed for managing game windows and handling input.
- **OpenGL**: Required for rendering game graphics.

You can install the necessary libraries using pip:

```bash
pip install pygame PyOpenGL
