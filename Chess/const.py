import pieces

DIM = (480, 480)
PIX = (DIM[0] // 8, DIM[1] // 8)

LIGHT = (255, 251, 184)
DARK = (0, 67, 128)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SELECTION = (192, 0, 0)

COL = {'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4', 'f': '5', 'g': '6', 'h': '7'}

PIECES = {'l': 'kqrbnp', 'd': 'KQRBNP'}

PIECE_MAP = {
    'k' : pieces.King,
    'q' : pieces.Queen,
    'r' : pieces.Rook,
    'b' : pieces.Bishop,
    'n' : pieces.Knight,
    'p' : pieces.Pawn
}