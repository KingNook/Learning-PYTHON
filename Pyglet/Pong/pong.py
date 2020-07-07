import pyglet
import constants


# Pong specific constants

WALL_WIDTH = 20

PADDLE_WIDTH = 20
PADDLE_HEIGHT = 160

# END

window = pyglet.window.Window(width = constants.WIDTH, height = constants.WIDTH)

fps_display = pyglet.window.FPSDisplay(window = window)

def pyrect(x, y, w, h, c = constants.WHITE):
    return pyglet.shapes.Rectangle(x = x, y = y, width = w, height = h, color = c)

def pycirc(x, y, r, c = constants.WHITE):
    return pyglet.shapes.Circle(x = x, y = y, radius = r, color = c)

class Ball:
    def __init__(self, r = 20, dx = 1, dy = 1):
        self.x = constants.WIDTH / 2
        self.y = constants.HEIGHT / 2
        self.r = r
        self.dx = dx
        self.dy = dy

    @property
    def bounds(self):
        return [self.x, self.y, self.x + self.r, self.y + self.r]

    @property
    def image(self):
        return pyrect(self.x, self.y, self.r, self.r)

    def draw(self):
        print(self.bounds)
        return self.image.draw()

    def update(self, dt):
        self.x += 3*self.dx
        self.y += 3*self.dy

class Wall:
    def __init__(self, x, y):
        self.image = pyrect(x, y, WALL_WIDTH, constants.HEIGHT)

    def draw(self):
        return self.image.draw()

class Paddle:
    # Starting y for the paddle
    paddle_y = (constants.HEIGHT - PADDLE_HEIGHT) // 2

    def __init__(self, x, dy = 1, dir = 0):
        self.x = x
        self.y = self.paddle_y
        self.dy = 0
        self.dir = 0

    @property
    def bounds(self):
        return [self.x, self.y, self.x + PADDLE_WIDTH, self.y +  PADDLE_HEIGHT]

    @property
    def image(self):
        return pyrect(self.x, self.y, PADDLE_WIDTH, PADDLE_HEIGHT)

    def draw(self):
        return self.image.draw()

    def update(self, dt):

        print(f'{self.y} - {self.dy} ({self.dir})')
        # DIR should be +ve if upwards or -ve if downwards
        self.y += self.dy

        # Adjust DIR
        self.dy += self.dir
        if self.dir == 0:
            if self.dy > 0:
                self.dy -= 1
            else:
                self.dy += 1 
            

left_wall = Wall(0, 0)
right_wall = Wall(constants.WIDTH - WALL_WIDTH, 0)

left_paddle = Paddle(60)
right_paddle = Paddle(constants.WIDTH - 60) 

ball = Ball()

@window.event
def on_key_press(symbol, modifiers):

    if symbol == pyglet.window.key.UP:
        right_paddle.dir += 1

    elif symbol == pyglet.window.key.DOWN:
        right_paddle.dir -= 1

    elif symbol == pyglet.window.key.W:
        left_paddle.dir += 1
    
    elif symbol == pyglet.window.key.DOWN:
        left_paddle.dir -= 1

@window.event
def on_key_release(symbol, modifiers):

    '''
    if symbol == pyglet.window.key.UP:
        right_paddle.dir -= 1

    elif symbol == pyglet.window.key.DOWN:
        right_paddle.dir += 1

    elif symbol == pyglet.window.key.W:
        left_paddle.dir -= 1
    
    elif symbol == pyglet.window.key.S:
        left_paddle.dir += 1
    '''
    

@window.event
def on_draw():
    window.clear()

    left_wall.draw() 
    right_wall.draw()

    left_paddle.draw()
    right_paddle.draw()

    ball.draw()

    fps_display.draw()

def window_update(dt):
    ball.update(dt)
    
    left_paddle.update(dt)
    right_paddle.update(dt)

pyglet.clock.schedule_interval(window_update, 0.02)
pyglet.app.run()