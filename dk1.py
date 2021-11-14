import pyglet
import pymunk
from pymunk.pyglet_util import DrawOptions
from math import degrees
from marble import marble

# Window and space setup
window = pyglet.window.Window(1400, 720, "DK", resizable=False)
options = DrawOptions()
space = pymunk.Space()
space.gravity = 0, -1000
marbles = []
batch = pyglet.graphics.Batch()

#Circle parameters
mass = 1
radius = 30
marble_img = pyglet.image.load('./res/marble1.png')
marble_img.anchor_x = marble_img.width // 2
marble_img.anchor_y = marble_img.height // 2

#First body
segment_shape = pymunk.Segment(space.static_body, (0,0), (800, 40), 2)
segment_shape.body.position = 500, 400
segment_shape.elasticity = 0.80 #Steel
segment_shape.friction = 1.0
space.add(segment_shape)

#Second body
segment_shape = pymunk.Segment(space.static_body, (0,60), (800, 40), 2)
segment_shape.body.position = 100, 100
segment_shape.elasticity = 0.8 #Steel
segment_shape.friction = 1.0
space.add(segment_shape)

@window.event
def on_mouse_press(x, y, button, modifier):
    # Add a marble
    marbleBody = marble(space, 100, (x, y))
    marbles.append(marbleBody)
    



@window.event
def on_draw():
    window.clear()
    space.debug_draw(options)
    # Handle marble drawing
    for locMarble in marbles:
        locMarble.draw()


def update(dt):
    space.step(dt)

    for locMarble in marbles:
        locMarble.update(space)
        # Add code to check if off the board
        if locMarble.body.position.y < -20:
            space.remove(locMarble.body, locMarble.shape)
            marbles.remove(locMarble)
            locMarble = None


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1.0/60.0)
    pyglet.app.run()