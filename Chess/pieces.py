import pygame, board, const, os
pygame.init()


path = os.getcwd().replace('\\', '/').replace('\\', '/')

class Piece:
    def __init__(self, piece, board, colour):
        self.colour = colour
        self.icon = pygame.image.load(f'{path}/Chess/pieces/Chess_{piece.lower()}{colour}t60.png')
        if not isinstance(board, board.Board):
            raise TypeError
        self.board = board
    
    # Returns int from -1 to 1
    # Takes coord as tuple (x, y) and colour as string 'l' (white piece) or string 'd' (black piece)
    # -1 = Invalid move (out of bounds OR friendly piece)
    # 0 = Empty Square
    # 1 = Enemy piece
    def valid_square(self, coord, colour):
        # Check numbers are valid (within board)
        if not (0 <= coord[0] <= 7 and 0 <= coord[1] <= 7):
            return -1

        square = self.board[coord[0], coord[1]]

        # Check board space is clear
        if self.board[coord[0], coord[1]] == '0':
            return 0

        # Check piece occupying the square is of the opposite colour
        if square in const.PIECES[colour]:
            return -1
        
        return 1


class King(Piece):
    def __init__(self, board, colour):
        super().__init__('k', board, colour)

    # Moves a King can make from position (a, b)
    def moves(self, a, b, c):
        # Available moves
        m = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if not i == j == 0]

        valid_moves = []

        for move in m:
            state = super().valid_square(move, c)
            if state != -1:
                valid_moves.append(move)

        return valid_moves
        

class Queen(Piece):
    def __init__(self, board, colour):
        super().__init__('q', board, colour)

    def valid_square(self, coord, colour):
        return super().valid_square(coord, colour)

    # Moves a queen of colour c [string 'l' or string 'd'] can make from position (a, b)
    def moves(self, a, b, c):
        m = []
        
        x = a - 1
        # Horizontally to left
        while self.valid_square((x, b), c) == 0:
            m.append((x, b))
            x -= 1
        if self.valid_square((x, b), c) == 1:
            m.append((x, b))

        # Horizontally to right
        x = a + 1
        while self.valid_square((x, b), c) == 0:
            m.append((x, b))
            x += 1
        if self.valid_square((x, b), c) == 1:
            m.append((x, b))

        # Vertically upwards
        y = b - 1
        while self.valid_square((a, y), c) == 0:
            m.append((a, y))
            x -= 1
        if self.valid_square((a, y), c) == 1:
            m.append((a, y))
        
        # Vertically downwards
        y = b - 1
        while self.valid_square((a, y), c) == 0:
            m.append((a, y))
            x -= 1
        if self.valid_square((a, y), c) == 1:
            m.append((a, y))

        return m

class Rook(Piece):
    def __init__(self, board, colour):
        super().__init__('r', board, colour)

class Bishop(Piece):
    def __init__(self, board, colour):
        super().__init__('b', board, colour)

class Knight(Piece):
    def __init__(self, board, colour):
        super().__init__('n', board, colour)

class Pawn(Piece):
    def __init__(self, board, colour):
        super().__init__('p', board, colour)