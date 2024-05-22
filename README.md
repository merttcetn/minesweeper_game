# Minesweeper Game 💣

This project implements a simple Minesweeper game using Python and the Tkinter library. The game consists of a grid of cells, some of which contain mines. The objective is to uncover all the cells that do not contain mines without triggering any mines.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Modules](#modules)
  - [cell.py](#cellpy)
  - [minesweeper.py](#minesweeperpy)
  - [settings.py](#settingspy)
  - [utilities.py](#utilitiespy)

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/merttcetn/minesweeper_game
    ```
2. **Navigate to the project directory:**
    ```sh
    cd minesweeper
    ```
3. **Install the required dependencies:**
    ```sh
    pip install tkinter
    ```

## Usage

Run the main script to start the game:
```sh
python minesweeper.py
```

## Modules

### cell.py

This module contains the `Cell` class which represents each cell in the Minesweeper grid. The key functionalities of this class include:

- **Initialization:** Creating a cell with specific coordinates and determining if it is a mine.
- **Button Creation:** Creating a button for each cell in the grid.
- **Mine Randomization:** Randomly assigning mines to cells.
- **Click Actions:** Defining left-click and right-click behaviors, including revealing cells and marking potential mines.
- **Mine Counting:** Counting the number of surrounding mines for each cell.
- **Game Over Handling:** Displaying a message and exiting the game if a mine is clicked.

### minesweeper.py

This script sets up the main game window and frames using Tkinter, initializes the grid of cells, and starts the game loop. Key components include:

- **Main Window:** Configuring the main window with a title and size.
- **Frames:** Setting up top, left, and center frames for different UI elements.
- **Title Label:** Creating and placing the game title.
- **Grid Initialization:** Creating a grid of `Cell` objects and placing their buttons.
- **Mine Randomization:** Calling the method to randomly assign mines.
- **Cell Count Label:** Creating and placing a label to show the number of cells left.

### settings.py

This module defines various configuration settings for the game, including:

- **Window Dimensions:** Width and height of the game window.
- **Grid Size:** Size of the grid (number of cells per row and column).
- **Cell Count:** Total number of cells in the grid.
- **Mine Count:** Number of mines in the grid, determined as a fraction of the total cell count.
- **Win Count:** Number of cells that need to be uncovered to win the game.

### utilities.py

This module provides utility functions to calculate percentages of the window dimensions, which are used for layout purposes:

- **height_percentage(percentage):** Returns the height corresponding to a given percentage of the total window height.
- **width_percentage(percentage):** Returns the width corresponding to a given percentage of the total window width.

---

Enjoy playing Minesweeper! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
