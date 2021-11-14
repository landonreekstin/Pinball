import pyglet
from math import degrees
from pymunk.vec2d import Vec2d
from pyglet.gl import *

score_img = pyglet.image.load("./marble/res/numbers.png")
score_width = 36
score_height = 50
score_start_x = 55
score_start_y = 260 #260

class score():
    def updateScoreDiff(self, score):
        self.numScore += score
        self.tupScore = [int(d) for d in str(self.numScore)]

    def __init__(self, score):
            # string representation of score value
        self.numScore = 0
        self.tupScore = ()
        self.updateScoreDiff(score)

    def draw(self, position):
        drawingNo = 0
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        for item in self.tupScore:
            # Draw the graphic cooresponding with that
            # item's number
            region = score_img.get_region(score_start_x + (item * score_width), 
                score_start_y, score_width, score_height)
            region.blit(position.x+(drawingNo*score_width), position.y)
            drawingNo+=1

