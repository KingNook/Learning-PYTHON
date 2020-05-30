from mandelbrot import Mandelbrot
from PIL import Image, ImageDraw
import os

if os.path.isfile('./Graphing/Output/Mandelbrot.png'):
    os.remove('./Graphing/Output/Mandelbrot.png')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DIMENSIONS = (1000, 1000)

M_Graph = Mandelbrot(1000, R_S = -2, R_E = 1, I_S = -2, I_E = 1)

image = Image.new('RGB', DIMENSIONS, BLACK)
draw = ImageDraw.Draw(image)

for x in range(DIMENSIONS[0]):
    for y in range(DIMENSIONS[1]):
        color = 255 - M_Graph.graph[y, x]
        draw.point([x, y], (color, color, color))

image.save('./Graphing/Output/Mandelbrot.png', 'PNG')