import pygame, const
from board import Board

pygame.init()
pygame.display.set_caption('Chess')
screen = pygame.display.set_mode(const.DIM)

board = Board(screen)

# Remove after debugging
board.parse('00000000/00000000/0000q000/00000000/00000000/00000000/00000000/00000000 w KQkq - 0 1')

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

    board.draw_board()

    pygame.display.flip()