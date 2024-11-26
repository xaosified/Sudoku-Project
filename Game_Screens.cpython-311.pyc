import pygame
import sys
import sudoku_generator
import pygame, random
import pygame, random, sys
from sudoku_generator import *
pygame.init()


WIDTH = 700   #SCREEN DIMENSIONS
HEIGHT = 800  #SCREEN DIMENSIONS
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku!")


BUTTON_COLOR = (199, 119, 0)   #DARK ORANGE COLOR = USE SAME RGB COLOR MOVING FOAWRD
TEXT_COLOR = (255, 255, 255)   #WHITE
outline_color = (0, 0, 0)      # BLACK
title_color = (255, 255, 255)  # WHITE
BUTTON_WIDTH = 130
BUTTON_HEIGHT = 50
title_font = pygame.font.Font(None, 100)
font = pygame.font.Font(None, 60)

#Cell constants
GRID_SIZE = 9
CELL_SIZE = 77
BACKGROUND_COLOR = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
BUTTON_OUTLINE_COLOR = (0, 0, 0)
BUTTON_FONT = pygame.font.Font(None, 40)


#=====  3 classes below =======(start screen, board, end screen)====(start an dend screens are similar)============
#=======Most work on this file includes adding function to buttons creating a functioning board====================


class StartScreen:
    def __init__(self, screen):
        self.screen = screen
        self.width = WIDTH
        self.height = HEIGHT
        self.difficulty = None

    def draw_button(self, text, y_pos):
        text_surface = font.render(text, True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=(self.width // 2, y_pos))  # CENTER TEXT

        button_width = text_surface.get_width() + 40
        button_height = text_surface.get_height() + 40
        button_surface = pygame.Surface((button_width, button_height))
        button_surface.fill(BUTTON_COLOR)  #COLOR BUTTON
        pygame.draw.rect(button_surface, outline_color, button_surface.get_rect(), 5)  #OUTLINE BUTTON

        self.screen.blit(button_surface,  #DRAW BUTTON
                         (self.width // 2 - button_width // 2, y_pos - button_height // 2))  #POSITION BUTTON
        self.screen.blit(text_surface, text_rect)  # POSITION BUTTON TEXT

    def draw_title(self):
        title_text = title_font.render("Sudoku!", True, title_color)
        title_rect = title_text.get_rect(center=(self.width // 2, 120))
        title_outline = title_font.render("Sudoku!", True, outline_color)

        self.screen.blit(title_outline, title_rect.move(4, 4))   #OUTLINE OFFSET
        self.screen.blit(title_outline, title_rect.move(-4, -4)) #FOR
        self.screen.blit(title_outline, title_rect.move(4, -4))  #EACH
        self.screen.blit(title_outline, title_rect.move(-4, 4))  #CORNER
        self.screen.blit(title_text, title_rect)

    def handle_click(self, event):
        easy_rect = pygame.Rect(self.width // 2 - 120, self.height // 2 - 140, 240, 120)  #DEFINE
        medium_rect = pygame.Rect(self.width // 2 - 120, self.height // 2 - 40, 240, 120) #IF CLICKED
        hard_rect = pygame.Rect(self.width // 2 - 120, self.height // 2 + 60, 240, 120)   #AREAS


        if easy_rect.collidepoint(event.pos):  #CHECK IF CLICKED SYSTEM; update: return boolean for whether anything was clicked or not
            print("Easy Game Selected!")
            self.difficulty = 0
            return True
        elif medium_rect.collidepoint(event.pos):
            print("Medium Game Selected!")
            self.difficulty = 1
            return True
        elif hard_rect.collidepoint(event.pos):
            print("Hard Game Selected!")
            self.difficulty = 2
            return True
        return False

    def display(self): #Edit: now returns difficulty depending on which button was clicked
        while True:  #STARTSCREEN LOOP
            self.screen.fill((255, 200, 150)) #LIGHT ORANGE BACKGROUND COLOR = TO BE USED MOVING FORWARD
            self.draw_title()
            self.draw_button("Easy", self.height // 2 - 100)  # Easy button position
            self.draw_button("Medium", self.height // 2)  # Medium button position
            self.draw_button("Hard", self.height // 2 + 100)  # Hard button position

            for event in pygame.event.get():    #EVENT HANDLING
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.handle_click(event):
                        return self.difficulty

            pygame.display.update()



class SudokuBoard:
    def __init__(self, screen):
        self.screen = screen
        self.width = WIDTH
        self.height = HEIGHT
        self.board = [[0 for i in range(GRID_SIZE)] for _ in range(GRID_SIZE)]  # Initialize a 9x9 grid (empty)

    def draw_grid(self):
        self.screen.fill(BACKGROUND_COLOR)
        for row in range(GRID_SIZE):   #GRID LINES
            for col in range(GRID_SIZE):
                rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, LINE_COLOR, rect, 1)  # THIN LINE

        for row in range(0, 9, 3):  # SUBGRIDS
            for col in range(0, 9, 3):
                rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, 3 * CELL_SIZE, 3 * CELL_SIZE)
                pygame.draw.rect(self.screen, LINE_COLOR, rect, 3)  # THICK LINE

    def draw_button(self, text, x_pos, y_pos):
        text_surface = BUTTON_FONT.render(text, True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=(x_pos, y_pos))
        button_surface = pygame.Surface((BUTTON_WIDTH, BUTTON_HEIGHT))
        button_surface.fill(BUTTON_COLOR)
        pygame.draw.rect(button_surface, BUTTON_OUTLINE_COLOR, button_surface.get_rect(), 5)
        self.screen.blit(button_surface, (x_pos - BUTTON_WIDTH // 2, y_pos - BUTTON_HEIGHT // 2))
        self.screen.blit(text_surface, text_rect)

    def click_button(self, event):
        reset_rect = pygame.Rect(self.width // 4 - BUTTON_WIDTH // 2, self.height - 70, BUTTON_WIDTH, BUTTON_HEIGHT)
        restart_rect = pygame.Rect(self.width // 2 - BUTTON_WIDTH // 2, self.height - 70, BUTTON_WIDTH, BUTTON_HEIGHT)
        exit_rect = pygame.Rect(self.width * 3 // 4 - BUTTON_WIDTH // 2, self.height - 70, BUTTON_WIDTH, BUTTON_HEIGHT)
        if reset_rect.collidepoint(event.pos):
            print("Resetting")
            return "reset"
        elif restart_rect.collidepoint(event.pos):
            print("Restarting!")
            return "restart"
        elif exit_rect.collidepoint(event.pos):
            print("Exiting")
            pygame.quit()
            sys.exit()
        return None

    def display_board(self):
        while True:
            self.draw_grid()
            self.draw_button("Reset", self.width // 4, self.height - 40)    # RESET
            self.draw_button("Restart", self.width // 2, self.height - 40)  # RESTART
            self.draw_button("Exit", self.width * 3 // 4, self.height - 40) # EXIT

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    action = self.click_button(event)
                    if action == "reset":
                        self.reset_board()  #***RESET BORD = ADD FUNCTION TO THIS***
                    elif action == "restart":
                        self.reset_board()  #***RESTART GAME = ADD FUNCTION TO THIS***
                    elif action == "exit":
                        pygame.quit()
                        sys.exit()          #IS THIS GOOD? OR DO WE WANT IT TO GO TO THE GAME OVER SCREEN
            pygame.display.update()


def main_board():
    sudoku_board = SudokuBoard(screen)
    sudoku_board.display_board()





class EndScreen:
    def __init__(self, screen):
        self.screen = screen
        self.width = WIDTH
        self.height = HEIGHT

    def draw_button(self, text, y_pos):
        text_surface = font.render(text, True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=(self.width // 2, y_pos))  #CENTER TEXT
        button_width = text_surface.get_width() + 40
        button_height = text_surface.get_height() + 40         #VERY SIMILAR CODE COMPARED TO STARTSCREEN CLASS
        button_surface = pygame.Surface((button_width, button_height))
        button_surface.fill(BUTTON_COLOR)
        pygame.draw.rect(button_surface, outline_color, button_surface.get_rect(), 5)
        self.screen.blit(button_surface,
                         (self.width // 2 - button_width // 2, y_pos - button_height // 2))
        self.screen.blit(text_surface, text_rect)

    def draw_title(self, message):
        title_text = title_font.render(message, True, title_color)  #TITLE TEXT
        title_rect = title_text.get_rect(center=(self.width // 2, 150))
        title_outline = title_font.render(message, True, outline_color)  #TITLE OUTLINE

        self.screen.blit(title_outline, title_rect.move(4, 4))
        self.screen.blit(title_outline, title_rect.move(-4, -4))
        self.screen.blit(title_outline, title_rect.move(4, -4))
        self.screen.blit(title_outline, title_rect.move(-4, 4))
        self.screen.blit(title_text, title_rect)

    def handle_click(self, event):
        exit_rect = pygame.Rect(self.width // 2 - 120, self.height // 2 + 60, 240, 120)
        restart_rect = pygame.Rect(self.width // 2 - 120, self.height // 2 - 60, 240, 120)

        if exit_rect.collidepoint(event.pos):  #IF CLICKED SYSTEM = ***BOTH BUTTONS CURRENTLY QUIT GAME***
            print("EXIT GAME")
            pygame.quit()
            sys.exit()
        elif restart_rect.collidepoint(event.pos):
            print("Restart GAME") #***MAKE THIS BUTTON LOOP TO RESHOW THE START SCREEN***
            return True
        return False

    def display(self, game_won=True):
        while True:
            self.screen.fill((255, 200, 150))


            if game_won:
                message = "Game Won!  :)"    #WIN SCREEN TITLE
            else:
                message = "Game Over!  :("   #LOSE SCREEN TITLE
            self.draw_title(message)

            self.draw_button("Exit", self.height // 2 + 100)  # EXIT BUTTON
            self.draw_button("Restart", self.height // 2 - 20)  # RESTART BUTTON


            for event in pygame.event.get():   #EVENT HANDLING
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.handle_click(event):
                        return True

            pygame.display.update()


def main_endscreen():
    end_screen = EndScreen(screen)
    game_won = True
    while True:
        if end_screen.display(game_won):
            print("RESTART GAME")
            break  #***REST GAME HERE***
