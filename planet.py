from pygame import *

import Box2D  # The main library
# Box2D.b2 maps Box2D.b2Vec2 to vec2 (and so on)
from Box2D.Box2D import *

from camera import Camera
from settings import Settings

class Entity():
    world: b2World
    camera: Camera

    body: b2Body

    def __init__(self, world: b2World, camera: Camera, position: b2Vec2, radius: int):
        super().__init__()

        self.world = world
        self.camera = camera

        self.body = self.world.CreateStaticBody(
            position=position,
            shapes=b2CircleShape(radius=radius),
        )
 
    def get_position(self):
        return b2Vec2(self.body.position[0], self.body.position[1])
    
    def update(self):
        pass

    def draw(self):
        self.camera.color = Color(255, 0, 0)
        self.camera.render(self.body)
