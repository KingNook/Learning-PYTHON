import pygame
import colors

pygame.init()

def is_white(x, y):
    if x % 2 == y % 2:
        return colors.WHITE
    else:
        return colors.BLACK

def rect(a, b):
    return pygame.Rect(PIX[0] * x, PIX[1] * y, PIX[0], PIX[1])

DIMENSIONS = (240, 240)
PIX = (DIMENSIONS[0] // 8, DIMENSIONS[1] // 8)

screen = pygame.display.set_mode(DIMENSIONS)
screen.fill(colors.WHITE)

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    for x in range(8):
        for y in range(8):
            pygame.draw.rect(screen, is_white(x, y), rect(x, y))

    pygame.display.flip()

pygame.quit()