from mandelbrot import Mandelbrot
from PIL import Image, ImageDraw

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DIMENSIONS = (600, 600)

M_Graph = Mandelbrot(600)

palette = []

image = Image.new('RGB', DIMENSIONS, WHITE)
draw = ImageDraw.Draw(image)

for x in range(DIMENSIONS[0]):
    for y in range(DIMENSIONS[1]):
        color = M_Graph.graph[y, x]
        draw.point([x, y], (color, color, color))

image.save('./Graphing/Output/Mandelbrot.png', 'PNG')