import pyglet

DIM = (640, 640)
PIX = (DIM[0] / 256, DIM[1] / 256)

window = pyglet.window.Window(*DIM)

@window.event
def on_show():
    print('Start')

    for x in range(255):
        for y in range(255):
            pixel = pyglet.shapes.Rectangle(x*PIX[0], y*PIX[1], PIX[0], PIX[1], ((x+y)%256, (x-y)%256, x))
            pixel.draw()

    print('Done')

pyglet.app.run()