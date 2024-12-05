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
COMPLETE_SIZE = pygame.font.Font(None, 35) #size of the number within each cell
SKETCH_SIZE = pygame.font.Font(None, 30) #size of sketched number; needs to be in the top left of the cell and smaller
#Edit: complete and sketch size changed 

class Cell:

    def __init__(self, editable, value, row, col, screen):
        #Constructor for the Cell class
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

        self.sketched_value = 0
        self.is_selected = False

        self.editable = editable



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
        x = self.row * CELL_SIZE #the (x,y) coords will be at the top left of the cell selected
        y = self.col * CELL_SIZE

        #Need to create the red box around the cell selected and display the number typed in
        if self.is_selected:
            pygame.draw.rect(self.screen, SELECT_COLOR, (x, y, 75, 75), 3) #draws red box around cell selected
        else:
            pass #doesn't draw an outline if the cell isnt selected

        if self.value != 0: #value when fully typed in; in black
            num_surface = COMPLETE_SIZE.render(str(self.value), True, COMPLETE_COLOR)
            self.screen.blit(num_surface, (x + 30, y + 25)) #Edit: x value changed to keep it on center

        elif self.sketched_value != 0 and self.value == 0: #value for when the number is sketched; in grey
            sketch_surface = SKETCH_SIZE.render(str(self.sketched_value), True, SKETCH_COLOR)
            self.screen.blit(sketch_surface, (x + 5, y + 5))


#-------------------------------------------------------------------------------------------------------------


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.screen = screen
        self.width = WIDTH
        self.height = HEIGHT

        self.difficulty = difficulty
        difficulty_rmv = [30, 40, 50] #0 for easy, 1 for medium, 2 for hard; determiend by output of StartScreen class in main

        self.generated_board = generate_sudoku(9, difficulty_rmv[difficulty]) #<== IMPORTANT: will be used as the board
        #self.generated_board = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                                #[6, 7, 2, 1, 9, 5, 3, 4, 8],
                                #[1, 9, 8, 3, 4, 2, 5, 6, 7],
                                #[8, 5, 9, 7, 6, 1, 4, 2, 3],
                                #[4, 2, 6, 8, 5, 3, 7, 9, 1],
                                #[7, 1, 3, 9, 2, 4, 8, 5, 6],
                                #[9, 6, 1, 5, 3, 7, 2, 8, 4],
                                #[2, 8, 7, 4, 1, 9, 6, 3, 5],
                                #[3, 4, 5, 2, 8, 6, 1, 7, 0]] #test board; all but 1 solved in order to test win and lose screens
        self.board = [] #<== will be the board with each cell being a class
        
        for row in range(9):
            rows = []
            for col in range(9):
                if self.generated_board[row][col] == 0:
                    cell = Cell(True,self.generated_board[row][col], row, col, screen)
                    rows.append(cell)
                else:
                    cell = Cell(False,self.generated_board[row][col], row, col, screen) #user cannot edit numbers that are already generated on the board
                    rows.append(cell)
            self.board.append(rows)
        
        self.selected_cell = None
    
    def draw_cells(self):
        for row in range(9):
            for col in range(9):
                self.board[row][col].draw()

    def select(self, row, col):
        if self.selected_cell: #for deselecting the cell
            self.selected_cell.is_selected = False

        self.selected_cell = self.board[row][col]
        self.selected_cell.is_selected = True #Board stores Cell classes <=== REMEMBER THIS

        if self.selected_cell.editable: #Only draws if the selected cell is editable <== NOT WORKING, please fix
            self.selected_cell.draw()

    def click(self, x, y):
        #checks if a click on the board is within the bounds of the board
        #used for validation in selecting the which cell to put the number in
        if 0 <= x <= 675 and 0 <= y <= 675:
            col = x // 75
            row = y // 75

            return (col, row)
        return None

    #The rest of the methods should follow the instructions. Good Luck!

    def clear(self):
    	#Clears the value cell.
        #Note that the user can only remove the cell values and sketched values that are filled by themselves.
        if self.selected_cell and self.selected_cell.editable:
            self.selected_cell.set_cell_value(0)
            self.selected_cell.set_sketched_value(0)
            self.board[self.selected_cell.row][self.selected_cell.col].set_cell_value(0)
            self.update_board()


    def sketch(self, value):
	    #Sets the sketched value of the current selected cell equal to the user entered value.
	    #It will be displayed at the top left corner of the cell using the draw() function.
        if self.selected_cell and self.selected_cell.editable and self.selected_cell.value == 0 and self.selected_cell.sketched_value == 0:
            self.selected_cell.set_sketched_value(value)
            self.selected_cell.draw()

    def place_number(self, value):
        #Sets the value of the currrent selected cell equal to the user entered value.
        #Called when the user presses the enter key
        if self.selected_cell.editable and self.selected_cell.value == 0:
            self.selected_cell.set_cell_value(value)
            self.board[self.selected_cell.row][self.selected_cell.col].set_cell_value(value)
            self.selected_cell.set_sketched_value(0)
            self.update_board()

    def reset_to_original(self):
        #Resets all cells in the board to their original values (0 if cleared, otherwise the corresponding digit).
        for row in range(9):
            for col in range(9):
                if self.board[row][col].editable:
                    self.board[row][col].value = 0
                    self.board[row][col].selected_value = 0
        self.draw_cells()
        self.update_board()

    def is_full(self):
        #Returns a Boolean value indicating whether the board is full or not.
        for i in range(9):
            for j in range(9):
                if self.board[i][j].value == 0:
                    return False
        return True

    def update_board(self):
        #Updates the underlying 2D board with the values in all cells.
        for row in range(9):
            for col in range(9):
                self.generated_board[row][col] = self.board[row][col].value

    def find_empty(self):
        #Finds an empty cell and returns its row and col as a tuple(x, y).
        for row in range(9):
            for col in range(9):
                if self.board[row][col].value == 0:
                    x = col * CELL_SIZE
                    y = row * CELL_SIZE
                    return (x, y)
        return None

    def check_board(self):
        #Check whether the Sudoku board is solved correctly.

        
        if self.is_full():
            self.update_board()
            valid_set = set(range(1, 10)) #compared to every row, column, and 3x3 box

            #checks if rows are solved
            for row in range(9):
                if set(self.generated_board[row]) != valid_set:
                    return False
            
            #checks if columns are solved
            for col in range(9):
                current_column = [self.generated_board[row][col] for row in range(9)]
                if set(current_column) != valid_set:
                    return False
            


            #checks if 3x3 boxes are solved
            for col in range(0, 9, 3):
                for row in range(0, 9, 3):
                    curr_box = [] #resets box
                    for i in range(3): #box has 3 diff levels to iterate through
                        curr_box.extend(self.generated_board[row + i][col:col+3]) #creates an array of 3x3 box
                    if set(curr_box) != valid_set:
                        return False
            
            return True
        return False #if the board is not filled


#================================================================================================================

#MAIN
#In addition to the above classes, students will have a sudoku.py file, where the main function will be run.
#This file will contain code to create the different screens of the project (game start, game over, and game
# in progress), and will form a cohesive project together with the rest of the code.
