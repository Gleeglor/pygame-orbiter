import math as Math
from Box2D.Box2D import *
from pygame import *

from camera import Camera
from settings import Settings

class Entity():
    rect: Rect
    color: Color
    canvas: Surface
    
    body: b2Body
    camera: Camera

    movement_speed: int
    rotation_speed: int

    def __init__(self, world: b2World, camera: Camera):
        self.movement_speed = 5
        self.rotation_speed = 1

        self.rect = Rect(0, 0, 20, 20)
        self.camera = camera

        self.color = Color(0, 255, 0)

        # Create a dynamic body
        self.body: b2Body = world.CreateDynamicBody(position=(0, 0), angle=0)

        self.settings = Settings()

        # And add a box fixture onto it (with a nonzero density, so it will move)
        self.box = self.body.CreatePolygonFixture(box=(1, 1), density=1, friction=0.3)

    def get_position(self):
        return b2Vec2(self.body.position[0], self.body.position[1])
 
    def update(self):
        pressed_keys = key.get_pressed()

        angle = self.body.angle - b2_pi / 2
        direction: b2Vec2 = b2Vec2(Math.cos(angle), Math.sin(angle))
        direction = direction.__imul__(1)

        if pressed_keys[K_w]:
            self.body.ApplyLinearImpulse(direction, self.body.worldCenter, True)
        if pressed_keys[K_s]:
            self.body.ApplyLinearImpulse(-direction, self.body.worldCenter, True)
         
        if pressed_keys[K_a]:
            self.body.ApplyAngularImpulse(-self.rotation_speed, True)
        if pressed_keys[K_d]:
            self.body.ApplyAngularImpulse(self.rotation_speed, True)
 
    def draw(self):
        self.camera.color = Color(0, 255, 0)
        self.camera.render(self.body)
