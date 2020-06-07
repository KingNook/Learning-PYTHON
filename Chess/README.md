# MULTI - OBJECT BRANCH
- For each piece in the FEN, initialise the piece
    - ## PIECE CLASS
        - [ ] Change piece to take its own position as well in \__init__()
        - [ ] Change piece methods to use instance variables for position
        - [ ] Change piece methods to use instance variable for color
    - ## BOARD CLASS
        - [ ] Change get_pieces method to create instances of pieces for each piece in the FEN
        - [ ] Change parse method to ?

# URGENT
- Currently broken - To fix
    - [ ] Initialise

# TODO
- [ ] Fix parse so that it takes proper FEN notation (currently has spaces = '0')
- [x] Finish parse (to parse FEN script to board state)

- [ ] Tidy up code for Queen.moves() (pieces.py)
- [ ] Change color of square for possible moves (board.py)
- [ ] Ensure color matches piece selected in board.select() (board.py)