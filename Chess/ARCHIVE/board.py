import pygame, const, os, numpy
pygame.init()

path = os.getcwd().replace('\\', '/').replace('\\', '/')

def get_coords(a, b):
    return (a * const.PIX[0], b * const.PIX[1])

def square(a, b):
    return pygame.Rect(const.PIX[0] * a, const.PIX[1] * b, const.PIX[0], const.PIX[1])

def is_white(a, b):
    if a % 2 == b % 2:
        return const.LIGHT
    else:
        return const.DARK

class Board:
    def __init__(self, display, position = None):
        self.pieces = {}
        self.board = numpy.zeros((8, 8), str)
        self.display = display
        self.selection = None

        self.get_pieces()

        # Starting position
        self.fen = position if position else 'rnbqkbnr/pppppppp/00000000/00000000/00000000/00000000/PPPPPPPP/RNBQKBNR w KQkq - 0 1' # Proper FEN --> 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
        self.parse()

    # Takes individual args
    def __getitem__(self, *key):
        return self.board[key[0], key[1]]

    # Circle from top left corner
    # Unpack to the pygame.draw.circle function
    def circle(self, a, b):
        return (self.display, const.SELECTION, ((a + 0.5) * const.PIX[0], (b + 0.5) * const.PIX[1]))

    def mouse_handler(self, pos):
        square = (pos[0] // const.PIX[0], pos[1] // const.PIX[1])
        if self.board[square[1], square[0]] != '0':
            
            if self.selection == square:
                print(f'Already selected: {self.selection}')
                return True
            
            self.selection = square
            
            print(f'Selection: {self.selection}')
        else:
            print(f'No piece there: {self.selection}')

        self.select()
        
        return True

    # Pass in position of piece (tuple)
    def select(self):
        if self.selection == None:
            return False

        piece = const.PIECE_MAP[self.board[self.selection[1], self.selection[0]].lower()]

        # Change color to color of piece
        for move in piece.moves(piece, self.selection[0], self.selection[1], 'l'):
            # CHANGE COLOR OF POSSIBLE MOVES
            pygame.draw.rect(self.display, const.SELECTION, square(*move))

    def draw_board(self):

        # Draw squares
        for x in range(8):
            for y in range(8):
                pygame.draw.rect(self.display, is_white(x, y), square(x, y))
                
                if self.selection == (x, y):
                    pygame.draw.rect(self.display, const.SELECTION, square(x, y))

                piece = self.board[y, x]
                if piece != '0':
                    self.display.blit(self.pieces[piece], get_coords(x, y))

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
        board = [list(i) for i in pos.split('/')[::-1]]
        for y in range(8):
            for x in range(8):
                self.board[y, x] = board[y][x]

        return True