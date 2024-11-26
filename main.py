import pygame, random, sys
from sudoku_generator import *
from Game_Screens import *

WIDTH = 700
HEIGHT = 800


        

def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT)) #don't know dimensions yet
    pygame.display.set_caption("Sudoku")

    while True:
        start_screen = StartScreen(screen)
        difficulty = start_screen.display() #0 for easy, 1 for medium, 2 for hard

        if difficulty is not None:
            sudoku_board = SudokuBoard(screen)
            sudoku_board.display_board()



main()

