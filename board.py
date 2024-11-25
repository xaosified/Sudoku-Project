#Classes and Functions 
#---------------------

class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
	    #Constructor for the SudokuGenerator class.
	    #For the purposes of this project, row_length is always 9
	    #removed_cells could vary depending on the difficulty level chosen. (see “UI Requirements”).
        self.row_length = 9
        self.remove_cells = removed_cells
        self.board = [[_ for i in range(self.row_length)] for j in range(self.row_length)]

    def get_board(self):
        #Returns a 2D python list of numbers, which represents the board
        for i in range(len(self.board)-1):
            for j in range(len(self.board[i])):
                print(self.board[i][j], end=' ')
            print()

    def print_board(self):
	    #Displays the board to the console.
	    #This is not strictly required, but it may be useful for debugging purposes.
        pass

    def valid_in_row(self, row, num):
        #Returns a Boolean value.
        #Determines if num is contained in the given row of the board.
        pass

    def valid_in_col(self, col, num):
        #Returns a Boolean value.
        #Determines if num is contained in the given column of the board.
        pass

    def valid_in_box(self, row_start, col_start, num):
        #Returns a Boolean value.
        #Determines if num is contained in the 3x3 box from
        #(row_start, col_start) to (row_start+2, col_start+2).
        pass

    def is_valid(self, row, col, num):
	    #Returns if it is valid to enter num at (row, col) in the board.
	    #This is done by checking the appropriate row, column, and box.
        pass

    def fill_box(self, row_start, col_start):
	    #Randomly fills in values in the 3x3 box from
        #(row_start, col_start) to (row_start+2, col_start+2).
	    #Uses unused_in_box to ensure no values occur in the box more than once.
        pass

    def fill_diagonal(self):
	    #Fills the three boxes along the main diagonal of the board.
	    #This is the first major step in generating a Sudoku.
	    #See the Step 1 picture in Sudoku Generation for further explanation.
        pass

    def fill_remaining(self):
        #This method is provided for students.
	    #Fills the remaining squares in the board.
	    #It is the second major step in generating a Sudoku.
	    #This will return a boolean.
        pass

    def fill_values(self):
	    #This method is provided for students.
	    #It constructs a solution by calling fill_diagonal and fill_remaining.
        pass

    def remove_cells(self):
	    #This method removes the appropriate number of cells from the board.
	    #It does so by randomly generating (row, col) coordinates of the board and setting the value to 0.
        #Note: Be careful not to remove the same cell multiple times.
        #A cell can only be removed once.
        #This method should be called after generating the Sudoku solution.
        pass


    def generate_sudoku(size, removed):
	    #Note: This is a function outside the SudokuGenerator class.
	    #This function should also be implemented in sudoku_generator.py as it interacts with the class.
        #Given size and removed, this function generates and returns a size-by-size sudoku board.
        #The board has cleared removed number of cells.
        #This function should just call the constructor and appropriate methods from the SudokuGenerator class.
        pass

#---------------------------------------------------------------------------------------------------------

class Cell:

    def __init__(self, value, row, col, screen):
        #Constructor for the Cell class
        self.value = value
        self.row = row
        self.col = col

    def set_cell_value(self, value):
        #Setter for this cell’s value
        pass

    def set_sketched_value(self, value):
        #Setter for this cell’s sketched value
        pass

    def draw(self):
        #Draws this cell, along with the value inside it.
        #If this cell has a nonzero value, that (value is displayed. Otherwise, no) value is displayed in the cell.
        #The cell is outlined red if it is currently selected.
        pass


#-------------------------------------------------------------------------------------------------------------


class Board:
    def __init__(self, width, height, screen, difficulty):
        #onstructor for the Board class. screen is a
        #window from PyGame. difficulty is a variable to indicate if the user chose easy medium, or hard.
        pass

    def draw(self):
    	#Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
	    #Draws every cell on this board.
        pass

    def select(self, row, col):
	    #Marks the cell at (row, col) in the board as the current selected cell.
	    #Once a cell has been selected, the user can edit its value or sketched value.
        pass

    def click(self, row, col):
    	#If a tuple of (x,y) coordinates is within the displayed board,
        #this function returns a tuple of the (row, col) of the cell which was clicked.
        #Otherwise, this function returns None.
        pass

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

board = [['_' for i in range(9)] for j in range(9)]
for i in range(len(board)-1):
    for j in range(len(board[i])):
        print(board[i][j], end=' ')
    print()
