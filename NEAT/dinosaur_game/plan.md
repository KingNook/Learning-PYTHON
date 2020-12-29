# Classes
- Dinosaur
- Obstacle
- Ground
- Background

# Functionality
- Base & Obstacles will move, Dinosaur will remain still (could add left/right movement later?)
    - 1 sprite needed for base, although could try more with tiled textures?
    - start w/ 3 obstacle textures (double cactus (small), single cactus (large), double cactus (large))
- Dinosaur animated, (don't animate pterodactyl yet?)
    - 2 or 3 sprites needed: 2 running, 1 after hits obstacle (although could do without)
    - Require 2 ducking/running sprites if adding pterodactyls


# PLAN
- Program Classes inc
    - Global Constants: gravity, velocity (game speed), window dimensions
    - Class Variables: IMG lists
    - Instance Variables:
        - (Dinosaur): y, velocity, 
    - Methods: init, Move, Draw, Get Mask
    - 