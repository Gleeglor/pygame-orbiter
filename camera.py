
from Box2D.Box2D import *
from pygame import *
import math as Math

from settings import Settings

class Camera:

    surface: Surface
    target: b2Vec2
    color: Color = Color(255, 255, 255)
    zoom: float = 0.2

    def __init__(self, position, canvas):
        self.position = position
        self.surface = canvas

    def is_polygon(self, type):
        return type == 2
    
    def is_circle(self, type):
        return type == 0
    
    def _render_polygon(self, body: b2Body, fixture: b2Fixture):
        shape: b2PolygonShape = fixture.shape

        # local transformations
        vertices = [(vertice[0], -vertice[1]) for vertice in shape.vertices]
        
        # set position, scale, rotation
        vertices = [body.transform * vertice for vertice in vertices]

        # scale up to world size/screen space
        vertices = [self.world_position(vertice) for vertice in vertices]

        # follow
        vertices = [self.follow(vertice) for vertice in vertices]

        # center
        vertices = [self.center(vertice) for vertice in vertices]

        draw.polygon(self.surface, self.color, vertices)

    def _render_circle(self, body: b2Body, fixture: b2Fixture):
        shape: b2CircleShape = fixture.shape
        position = body.position + shape.pos

        position = self.world_position(position)
        position = self.follow(position)
        position = self.center(position)

        draw.circle(self.surface, self.color, position, shape.radius / self.zoom)

    # Render a box2d body
    def render(self, body: b2Body):
        for fixture in body.fixtures:
            fixture: b2Fixture
            if self.is_polygon(fixture.type):
                self._render_polygon(body, fixture)

            if self.is_circle(fixture.type):
                self._render_circle(body, fixture)


    def world_position(self, position: b2Vec2):
        return b2Vec2(position[0], position[1]) / self.zoom

    def center(self, position: b2Vec2):
        return b2Vec2(position[0] + Settings.screen_width / 2, position[1] + Settings.screen_height / 2)

    def follow(self, position: b2Vec2):
        target = self.world_position(self.target)

        return b2Vec2(position[0] - target.x, position[1] - target.y)

    def world_line(self, start: b2Vec2, end: b2Vec2):
        center = b2Vec2(Settings.screen_width/2, Settings.screen_height/2)
        
        draw.line(self.surface, self.color, start + center - self.position, end + center - self.position)
