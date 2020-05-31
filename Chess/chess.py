import pygame

class Board:
    def __init__(self, display, position = None):
        self.pieces = {}
        self.board = []
        self.display = display

        self.get_pieces()

        # Starting position
        self.fen = position if position else 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
        self.parse()

    def get_pieces(self):
        # White pieces
        self.pieces['k'] = pygame.image.load('/pieces/Chess_klt60.png')
        self.pieces['q'] = pygame.image.load('/pieces/Chess_qlt60.png')
        self.pieces['r'] = pygame.image.load('/pieces/Chess_rlt60.png')
        self.pieces['b'] = pygame.image.load('/pieces/Chess_blt60.png')
        self.pieces['n'] = pygame.image.load('/pieces/Chess_nlt60.png')
        self.pieces['p'] = pygame.image.load('/pieces/Chess_plt60.png')

        # Black pieces
        self.pieces['K'] = pygame.image.load('/pieces/Chess_kdt60.png')
        self.pieces['Q'] = pygame.image.load('/pieces/Chess_qdt60.png')
        self.pieces['R'] = pygame.image.load('/pieces/Chess_rdt60.png')
        self.pieces['B'] = pygame.image.load('/pieces/Chess_bdt60.png')
        self.pieces['N'] = pygame.image.load('/pieces/Chess_ndt60.png')
        self.pieces['P'] = pygame.image.load('/pieces/Chess_pdt60.png')

        return True

    def parse(self, fen = None):
        # Use default starting position if none provided
        fen = fen if fen else self.fen

        pos, move, castle, en_passant, halfmove, fullmove = fen.split(' ')
        self.board = [list(i) for i in pos.split('/')]