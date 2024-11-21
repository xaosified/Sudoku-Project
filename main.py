import pygame, random
from sudoku_generator import *

def start_screen(screen):
    pass

def main():
    pygame.init()

    screen = pygame.display.set_mode((700, 1000)) #don't know dimensions yet
    pygame.display.set_caption("Sudoku")

    start_screen(screen)

