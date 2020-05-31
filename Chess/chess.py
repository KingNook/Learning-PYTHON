import pygame

class Board:
    def __init__(self):
        self.white = {}
        self.black = {}

    def get_pieces(self):
        # White pieces
        self.white['K'] = pygame.image.load()