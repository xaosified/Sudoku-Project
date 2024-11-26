#Classes and Functions
import pygame
from sudoku_generator import *
from Game_Screens import *

#Cell constants
GRID_SIZE = 9
CELL_SIZE = 75
BACKGROUND_COLOR = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
BUTTON_OUTLINE_COLOR = (0, 0, 0)
BUTTON_FONT = pygame.font.Font(None, 40)
SKETCH_COLOR = (210, 210, 210) #Grey; for when the number is sketched in the cell
COMPLETE_COLOR = (0, 0, 0) #Black; for when the sketch is completely entered in
SELECT_COLOR = (204, 0, 0) #Red; colors the outline of the box when selected
#To do: font constants for letter size

class Cell:

    def __init__(self, value, row, col, screen):
        #Constructor for the Cell class
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

        self.sketched_value = 0
        self.is_selected = False



    def set_cell_value(self, value):
        #Setter for this cell’s value
        self.value = value

    def set_sketched_value(self, value):
        #Setter for this cell’s sketched value
        self.sketched_value = value

    def draw(self):
        #Draws this cell, along with the value inside it.
        #If this cell has a nonzero value, that (value is displayed. Otherwise, no) value is displayed in the cell.
        #The cell is outlined red if it is currently selected.
        x = self.col * CELL_SIZE
        y = self.row * CELL_SIZE

        #Need to create the red box around the cell selected and display the number typed in

        pass


#-------------------------------------------------------------------------------------------------------------


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.screen = screen
        self.width = WIDTH
        self.height = HEIGHT

        self.difficulty = difficulty
        difficulty_rmv = [30, 40, 50] #0 for easy, 1 for medium, 2 for hard; determiend by output of StartScreen class in main

        self.generated_board = generate_sudoku(9, difficulty_rmv[difficulty])
        self.board = []
        
        for row in range(9):
            rows = []
            for col in range(9):
                cell = Cell(self.generated_board[row][col], row, col, screen)
                rows.append(cell)
            self.cells.append(rows)
        
        self.selected_cell = None
    

    def select(self, row, col):
        pass

    def click(self, x, y):
        #checks if a click on the board is within the bounds of the board
        if 0 <= x <= 675 and 0 <= y <= 675:
            col = x // 75
            row = y // 75

            return (x,y)
        return None


    #The rest of the methods should follow the instructions. Good Luck!

    def clear(self):
    	#Clears the value cell.
        #Note that the user can only remove the cell values and sketched values that are filled by themselves.
        pass

    def sketch(self, value):
	    #Sets the sketched value of the current selected cell equal to the user entered value.
	    #It will be displayed at the top left corner of the cell using the draw() function.
        pass

    def place_number(self, value):
        #Sets the value of the currrent selected cell equal to the user entered value.
        #Called when the user presses the enter key
        pass

    def reset_to_original(self):
        #Resets all cells in the board to their original values (0 if cleared, otherwise the corresponding digit).
        pass

    def is_full(self):
        #Returns a Boolean value indicating whether the board is full or not.
        pass

    def update_board(self):
        #Updates the underlying 2D board with the values in all cells.
        pass

    def find_empty(self):
        #Finds an empty cell and returns its row and col as a tuple(x, y).
        pass

    def check_board(self):
        #Check whether the Sudoku board is solved correctly.
        pass

#================================================================================================================

#MAIN
#In addition to the above classes, students will have a sudoku.py file, where the main function will be run.
#This file will contain code to create the different screens of the project (game start, game over, and game
# in progress), and will form a cohesive project together with the rest of the code.
