import pygame, const
from chess import Board

pygame.init()
screen = pygame.display.set_mode(const.DIM)

board = Board(screen)
board.draw_board()