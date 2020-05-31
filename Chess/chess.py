import pygame

class Board:
    def __init__(self, position = None):
        self.white = {}
        self.black = {}

        self.get_pieces()

        # Starting position
        self.fen = position if position else 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'

    def get_pieces(self):
        # White pieces
        self.white['K'] = pygame.image.load('/pieces/Chess_klt60.png')
        self.white['Q'] = pygame.image.load('/pieces/Chess_qlt60.png')
        self.white['R'] = pygame.image.load('/pieces/Chess_rlt60.png')
        self.white['B'] = pygame.image.load('/pieces/Chess_blt60.png')
        self.white['N'] = pygame.image.load('/pieces/Chess_nlt60.png')
        self.white['P'] = pygame.image.load('/pieces/Chess_plt60.png')

        # Black pieces
        self.black['K'] = pygame.image.load('/pieces/Chess_kdt60.png')
        self.black['Q'] = pygame.image.load('/pieces/Chess_qdt60.png')
        self.black['R'] = pygame.image.load('/pieces/Chess_rdt60.png')
        self.black['B'] = pygame.image.load('/pieces/Chess_bdt60.png')
        self.black['N'] = pygame.image.load('/pieces/Chess_ndt60.png')
        self.black['P'] = pygame.image.load('/pieces/Chess_pdt60.png')

        return True

    def parse(self):
        return NotImplemented