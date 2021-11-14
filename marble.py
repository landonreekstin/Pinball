import pyglet
import pymunk
from pymunk.pyglet_util import DrawOptions
from math import degrees
from pymunk.vec2d import Vec2d

#Circle parameters
marble_img = pyglet.image.load('./res/marble1.png')
marble_img.anchor_x = marble_img.width // 2
marble_img.anchor_y = marble_img.height // 2

class marble:
    mass = 1
    radius = 30

    def __init__(self, space, id, newPosition):
        # Add circle
        circle_moment = pymunk.moment_for_circle(self.mass, 0, self.radius)
        self.body = pymunk.Body(self.mass, circle_moment)
        self.body.position = Vec2d(float(newPosition[0]), float(newPosition[1]))
        self.shape = pymunk.Circle(self.body, self.radius)
        self.shape.id = id
        self.shape.elasticity = 0.68 
        self.shape.friction = 0.68
        self.sprite = pyglet.sprite.Sprite(marble_img, *self.body.position)
        space.add(self.body, self.shape)

    def draw(self):
        if self.sprite != None:
            self.sprite.draw()

    def update(self, space):
        #Update the sprite position
        self.sprite.rotation = -degrees(self.body.angle)
        self.sprite.position = self.body.position
