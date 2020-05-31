import pygame, const
from chess import Board

pygame.init()
pygame.display.set_caption('Chess')
screen = pygame.display.set_mode(const.DIM)

board = Board(screen)
board.draw_board()

# GAME LOOP
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # if LMB
            if event.button == 1:
                board.mouse_handler(event.pos)

    pygame.display.flip()