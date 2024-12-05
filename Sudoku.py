import pygame, random, sys
from sudoku_generator import *
from Game_Screens import *
from board import *

WIDTH = 675
HEIGHT = 800


        

def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT)) #don't know dimensions yet
    pygame.display.set_caption("Sudoku")

    while True:
        start_screen = StartScreen(screen)
        difficulty = start_screen.display() #0 for easy, 1 for medium, 2 for hard

        if difficulty is not None:
            board = Board(WIDTH, HEIGHT, screen, difficulty)

            playing = True
            while playing:
                screen.fill(BACKGROUND_COLOR)
                game_screen = GameScreen(screen)
                game_screen.display_board()

                end_screen = EndScreen(screen)

                board.draw_cells()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        if 675 > y: #avoids the buttons created by game_screen
                            cell_index = board.click(x,y)
                            if cell_index:
                                row, col = cell_index
                                board.select(row, col) #draws red ring around selected cell
                        
                        button_pressed = game_screen.click_button(event)
                        if button_pressed == "reset":
                            board.reset_to_original()
                        elif button_pressed == "restart":
                            playing = False
                        elif button_pressed == "exit":
                            pygame.quit()
                            sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if board.selected_cell:
                            if event.key in range(pygame.K_1, pygame.K_9 + 1): #keys are stored in unicode
                                value = event.key - pygame.K_0 #subtracting unicode values gives true value of the key pressed
                                board.sketch(value)
                            elif event.key == pygame.K_RETURN: #puts the sketched numbers into actuality
                                board.place_number(board.selected_cell.sketched_value)
                            elif event.key == pygame.K_BACKSPACE: #deletes value in cell
                                board.clear()
                            if event.key == pygame.K_UP: #moves up 
                                col = (col - 1) % 9
                            elif event.key == pygame.K_DOWN: #moves down 
                                col = (col + 1) % 9
                            elif event.key == pygame.K_LEFT: #moves left
                                row = (row - 1) % 9
                            elif event.key == pygame.K_RIGHT: #moves right
                                row = (row + 1) % 9
                            board.select(row, col) #updates the selected cel
                if board.is_full():
                    if board.check_board():
                        end_screen.display(True)
                    else:
                        end_screen.display(False)
                    playing = False #will only run if user selects restarts, since it breaks the loop
                    #in end_screen

                pygame.display.update()

if __name__ == "__main__":
    main()

