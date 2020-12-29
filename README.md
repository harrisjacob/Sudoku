# 9x9 Sudoku Solver

## Description
The focus of this project was to create a 9x9 Sudoku solver as well as experiement with bitmap displays in the form of GUIs.  **sudokuCMD.py** requires the users to input their Sudoku puzzles into the list element in the main function then execute the Python script.  This was mainly used for algorithmic verification.  Within the **9x9GUI** directory, the **solve9x9.py** script spawns a GUI that the user can manually input puzzle data.

If no solution exists (i.e. the puzzle the user input is invalid) a warning is printed to the command line without a provided solution.

The **ProofOfConcept** directory contains some scripts used to demo some of the features of the textbox class as well as the Sudoku board bitmap drawing, both of which were later implemented in the **solve9x9.py** script.

## Use
PyGame must be installed to run the demo module.

## Implementation
The algorithm used in both **sudokuCMD.py** and **solve9x9.py** is a recursive backtracking algorithm.

## Future use and updates
Most of the current code is general enough that it could be used to solve any NxN Sudoku puzzle containing integer square root of N<sup>2</sup> (or simply N) boxes. I'm using the term boxes here as opposed to cells to describe the square sections in a Sudoku puzzle that must contain all N digits.  For a traditional 9x9 Sudoku puzzle, there are 9<sup>2</sup> cells and 9 boxes thus satisfying this requirement.

Future solvers might implement a different algorithm or simply solve 16x16 puzzles with a hexidecimal base.
