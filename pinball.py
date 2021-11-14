import pyglet
import pymunk
import sys
from pymunk.pyglet_util import DrawOptions
from math import degrees
from marble import marble
from pyglet.window import key

# Window and space setup
window = pyglet.window.Window(820, 900, "Pinball", resizable=False)
options = DrawOptions()
space = pymunk.Space()
space.gravity = 0, -1000
marbles = []
batch = pyglet.graphics.Batch()

#Ball parameters
mass = 1
radius = 30
ball_counter = 0
marble_img = pyglet.image.load('./res/marble1.png')
marble_img.anchor_x = marble_img.width // 2
marble_img.anchor_y = marble_img.height // 2


# Static Structures

#Borders
#left border
segment_shape = pymunk.Segment(space.static_body, (10,260), (10, 900), 2)
#segment_shape.body.position = 500, 400
segment_shape.elasticity = 0.80
segment_shape.friction = 1.0
space.add(segment_shape)

#right border
segment_shape = pymunk.Segment(space.static_body, (706,60), (706, 790), 2)
#segment_shape.body.position = 100, 100
segment_shape.elasticity = 0.80
segment_shape.friction = 1.0
space.add(segment_shape)

#top border
segment_shape = pymunk.Segment(space.static_body, (10,900), (706, 900), 2)
#segment_shape.body.position = 500, 400
segment_shape.elasticity = 0.80
segment_shape.friction = 1.0
space.add(segment_shape)

#left bottom diagonal
segment_shape = pymunk.Segment(space.static_body, (10,260), (180, 60), 2)
#segment_shape.body.position = 100, 100
segment_shape.elasticity = 0.80
segment_shape.friction = 1.0
space.add(segment_shape)

#right bottom diagonal
segment_shape = pymunk.Segment(space.static_body, (706,260), (536, 60), 2)
#segment_shape.body.position = 100, 100
segment_shape.elasticity = 0.80
segment_shape.friction = 1.0
space.add(segment_shape)

#right launch tube border
segment_shape = pymunk.Segment(space.static_body, (816,0), (816, 900), 2)
#segment_shape.body.position = 100, 100
segment_shape.elasticity = 0.80
segment_shape.friction = 1.0
space.add(segment_shape)

#launch tube bottom
segment_shape = pymunk.Segment(space.static_body, (816,0), (706, 0), 2)
#segment_shape.body.position = 100, 100
segment_shape.elasticity = 3.5
segment_shape.friction = 1.0
space.add(segment_shape)

#launch tube left bottom
segment_shape = pymunk.Segment(space.static_body, (706,00), (706, 60), 2)
#segment_shape.body.position = 100, 100
segment_shape.elasticity = 0.40
segment_shape.friction = 1.0
space.add(segment_shape)

#launch tube diagonal top
segment_shape = pymunk.Segment(space.static_body, (895,790), (706, 900), 2)
#segment_shape.body.position = 100, 100
segment_shape.elasticity = 1.0
segment_shape.friction = 1.0
space.add(segment_shape)


# Shapes
# Circles
segment_shape = pymunk.Circle(space.static_body, 30, (348, 600))
#segment_shape.body.position = 100, 100
segment_shape.elasticity = 2.0
segment_shape.friction = 0.4
space.add(segment_shape)

segment_shape = pymunk.Circle(space.static_body, 30, (198, 600))
#segment_shape.body.position = 100, 100
segment_shape.elasticity = 2.0
segment_shape.friction = 0.4
space.add(segment_shape)

segment_shape = pymunk.Circle(space.static_body, 30, (498, 600))
#segment_shape.body.position = 100, 100
segment_shape.elasticity = 2.0
segment_shape.friction = 0.4
space.add(segment_shape)

segment_shape = pymunk.Circle(space.static_body, 20, (288, 500))
#segment_shape.body.position = 100, 100
segment_shape.elasticity = 2.0
segment_shape.friction = 0.4
space.add(segment_shape)

segment_shape = pymunk.Circle(space.static_body, 20, (408, 500))
#segment_shape.body.position = 100, 100
segment_shape.elasticity = 2.0
segment_shape.friction = 0.4
space.add(segment_shape)

segment_shape = pymunk.Segment(space.static_body, (10, 360), (100, 280), 1)
#segment_shape.body.position = 100, 100
segment_shape.elasticity = 0.75
segment_shape.friction = 0.4
space.add(segment_shape)

segment_shape = pymunk.Segment(space.static_body, (706, 360), (616, 280), 1)
#segment_shape.body.position = 100, 100
segment_shape.elasticity = 0.75
segment_shape.friction = 0.4
space.add(segment_shape)


# stopper to prevent downward flipper movement
segment_shape = pymunk.Circle(space.static_body, 10, (280, 0))
#segment_shape.body.position = 100, 100
segment_shape.elasticity = 0.0
segment_shape.friction = 10.0
space.add(segment_shape)

# stopper to prevent downward flipper movement
segment_shape = pymunk.Circle(space.static_body, 10, (436, 0))
#segment_shape.body.position = 100, 100
segment_shape.elasticity = 0.0
segment_shape.friction = 10.0
space.add(segment_shape)


# Flippers

# Left Flipper
# Creating the flipper
l_moment = pymunk.moment_for_segment(100, (0,0), (0,110), 10)
l_flipper = pymunk.Body(100, l_moment)
l_flipper.position = (180, 40)
# Creating joint
l_flipper_pivot_pt_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
l_flipper_pivot_pt_body.position = l_flipper.position
l_flipper_joint = pymunk.PinJoint(l_flipper, l_flipper_pivot_pt_body, (0,0), (0,0))
l_flipper_joint.activate_bodies()
# Limit joint rotation
pymunk.RotaryLimitJoint(l_flipper, l_flipper_pivot_pt_body, -1/8, 1/8)
# Creating the physical shape of the flipper
l_flipper_shape = pymunk.Segment(l_flipper, (0, 0), (110, 0), 10)
# flipper properties and adding to space
l_flipper_shape.elasticity = 1.75
l_flipper_shape.friction = 1.0
space.add(l_flipper)
space.add(l_flipper_pivot_pt_body)
space.add(l_flipper_shape)
space.add(l_flipper_joint)


# Right Flipper
# Creating the flipper
r_moment = pymunk.moment_for_segment(100, (0,0), (0,110), 10)
r_flipper = pymunk.Body(100, r_moment)
r_flipper.position = (536, 40)
# Creating joint
r_flipper_pivot_pt_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
r_flipper_pivot_pt_body.position = r_flipper.position
r_flipper_joint = pymunk.PinJoint(r_flipper, r_flipper_pivot_pt_body, (0,0), (0,0))
r_flipper_joint.activate_bodies()
# Limit joint rotation
pymunk.RotaryLimitJoint(r_flipper, r_flipper_pivot_pt_body, -1/8, 1/8)
# Creating the physical shape of the flipper
r_flipper_shape = pymunk.Segment(r_flipper, (0, 0), (-110, 0), 10)
# flipper properties and adding to space
r_flipper_shape.elasticity = 1.75
r_flipper_shape.friction = 1.0
space.add(r_flipper)
space.add(r_flipper_pivot_pt_body)
space.add(r_flipper_shape)
space.add(r_flipper_joint)



##def on_mouse_press(x, y, button, modifier):
    # Add a marble
    #marbleBody = marble(space, 100, (x, y))
    #marbles.append(marbleBody)



@window.event
def on_key_press(symbol, modifiers):
    
    # ENTER: Spawns ball
    # Spawning ball in launch tube on enter when no other balls are on the board
    if len(marbles) == 0:
        if symbol == key.RETURN:
            marbleBody = marble(space, 100, (761, 790))
            marbles.append(marbleBody)
            
            # Incrementing ball counter
            global ball_counter
            ball_counter = ball_counter + 1

    # LEFT: Flips left flipper
    if symbol == key.LEFT:
        l_flipper.apply_impulse_at_local_point((0, 15000), (120, 0))

    # RIGHT: Flips right flipper
    if symbol == key.RIGHT:
        r_flipper.apply_impulse_at_local_point((0, 15000), (-120, 0))

    # DOWN: Moves both flippers down
    # Use this to reset your paddles when they float
    if symbol == key.DOWN:
        l_flipper.apply_impulse_at_local_point((0, -10000), (120, 0))
        r_flipper.apply_impulse_at_local_point((0, -10000), (-120, 0))



@window.event
def on_draw():
    window.clear()
    space.debug_draw(options)
    # Handle marble drawing
    for locMarble in marbles:
        locMarble.draw()


def update(dt):
    space.step(dt)

    global ball_counter

    for locMarble in marbles:
        locMarble.update(space)
        # Check if marble is off the board
        if locMarble.body.position.y < -20 or locMarble.body.position.y > 920 or locMarble.body.position.x < -20 or locMarble.body.position.x > 840:
            space.remove(locMarble.body, locMarble.shape)
            marbles.remove(locMarble)
            locMarble = None

        # Bronze Level code to end game
        # Change once score system implemented
        if ball_counter == 3 and len(marbles) == 0:
            sys.exit()



if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1.0/60.0)
    pyglet.app.run()