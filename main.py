import pygame, random, sys
from sudoku_generator import *

WIDTH = 700
HEIGHT = 800


def start_screen(screen):
    screen.fill('white')

    #Fonts and size
    TITLE_FONT = pygame.font.Font(None, 70)
    BUTTON_FONT = pygame.font.Font(None, 70)
    #creates titles
    title = TITLE_FONT.render("SUDOKU", 0, (0,0,0))
    title_rect = title.get_rect(center = (WIDTH // 2, HEIGHT // 2 - 200))
    screen.blit(title, title_rect)

    #text for the button
    easy_text = BUTTON_FONT.render("Easy", 0, (255, 255, 255))
    medium_text = BUTTON_FONT.render("Medium", 0, (255, 255, 255))
    hard_text = BUTTON_FONT.render("Hard", 0, (255, 255, 255))

    #creates the colored square and boundary for each button; also places the text within that the colored square
    easy_button = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_button.fill("blue")
    easy_button.blit(easy_text, (10, 10))
    medium_button = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_button.fill("blue")
    medium_button.blit(medium_text, (10, 10))
    hard_button = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_button.fill("blue")
    hard_button.blit(hard_text, (10,10))

    #location of each button
    easy_rect = easy_button.get_rect(center = (WIDTH // 2, HEIGHT // 2))
    medium_rect = medium_button.get_rect(center = (WIDTH // 2, HEIGHT // 2 + (175//2)))
    hard_rect = hard_button.get_rect(center = (WIDTH // 2, HEIGHT // 2 + 175))

    #places the button in said location
    screen.blit(easy_button, easy_rect)
    screen.blit(medium_button, medium_rect)
    screen.blit(hard_button, hard_rect)

    #user input
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rect.collidepoint(event.pos): #0 IF USER CLICKS EASY
                    return 0
                elif medium_rect.collidepoint(event.pos): #1 IF USER CLICKS MEDIUM
                    return 1
                elif hard_rect.collidepoint(event.pos): #2 IS USER CLICKS HARD
                    return 2
                else:
                    continue
        pygame.display.update()


        

def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT)) #don't know dimensions yet
    pygame.display.set_caption("Sudoku")

    while True:
        game_difficulty = start_screen(screen) #0 for east, 1 for medium, 2 for hard
        


main()

