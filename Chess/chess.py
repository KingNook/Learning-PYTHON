import pygame, const, os
pygame.init()

path = os.getcwd().replace('\\', '/').replace('\\', '/')

def square(a, b):
    return pygame.Rect(const.PIX[0] * a, const.PIX[1] * b, const.PIX[0], const.PIX[1])

def is_white(a, b):
    if a % 2 == b % 2:
        return const.WHITE
    else:
        return const.BLACK

class Board:
    def __init__(self, display, position = None):
        self.pieces = {}
        self.board = []
        self.display = display

        self.get_pieces()

        # Starting position
        self.fen = position if position else 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
        self.parse()

    def draw_board(self):
        for x in range(8):
            for y in range(8):
                pygame.draw.rect(self.display, is_white(x, y), square(x, y))

        return True

    def load_piece(self, piece, colour):
        self.pieces[piece] = pygame.image.load(f'{path}/Chess/pieces/Chess_{piece.lower()}{colour}t60.png')

        return True

    def get_pieces(self):
        # White pieces
        self.load_piece('k', 'l')
        self.load_piece('q', 'l')
        self.load_piece('r', 'l')
        self.load_piece('b', 'l')
        self.load_piece('n', 'l')
        self.load_piece('p', 'l')

        # Black pieces
        self.load_piece('K', 'd')
        self.load_piece('Q', 'd')
        self.load_piece('R', 'd')
        self.load_piece('B', 'd')
        self.load_piece('N', 'd')
        self.load_piece('P', 'd')

        return True

    def parse(self, fen = None):
        # Use default starting position if none provided
        fen = fen if fen else self.fen

        pos, move, castle, en_passant, halfmove, fullmove = fen.split(' ')
        self.board = [list(i) for i in pos.split('/')]

        return True