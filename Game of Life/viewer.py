import pygame
from sim import Grid, gg

g = Grid(100)

# dimensions for pygame viewer
DIMENSIONS = (550, 550)
PIX = (5, 5)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()

screen = pygame.display.set_mode(DIMENSIONS)

clock = pygame.time.Clock()

gg(g)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(WHITE)

    for i in range(g.x):
        for j in range(g.y):
            if g.get_cell(j, i):
                pygame.draw.rect(screen, BLACK, pygame.Rect(i*PIX[0]+25, j*PIX[1]+25, PIX[0], PIX[1]))

    pygame.display.flip()
    
    g.update()
    clock.tick(2)

pygame.quit()
