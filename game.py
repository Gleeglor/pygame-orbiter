import json
import sys
import math as Math
from pygame import *

from camera import Camera
import enemy
import planet
import player
from settings import Settings

import Box2D  # The main library
from Box2D.Box2D import *

from singleton import Singleton

class Game(metaclass=Singleton):
    settings = Settings()
    canvas: Surface
    world: b2World
    camera: Camera

    def __init__(self):
        self.screen = (self.settings.screen_width, self.settings.screen_height)

        self.canvas = display.set_mode(self.screen)
        self.camera = Camera(b2Vec2(0, 0), self.canvas)
        self.clear()

        self.FPS = self.settings.fps
        self.FramePerSec = time.Clock()

        display.set_caption(self.settings.window_caption)

        self.physics()

        self.planet = planet.Entity(self.world, self.camera, b2Vec2(0, 1500), 1500)
        self.player = player.Entity(self.world, self.camera)

    def physics(self):
        self.world = b2World(gravity=(0, 0), doSleep=True)

        # # And a static body to hold the ground shape
        # self.ground_body = self.world.CreateStaticBody(
        #     position=(-50, 0),
        #     shapes=b2PolygonShape(box=(100, 0.05)),
        # )


    def clear(self):
        self.canvas.fill(Color(255, 255, 255))

    def render(self):
        self.clear()
        self.planet.draw()
        self.player.draw()


        self.camera.color = (220, 220, 220)
        # self.camera.world_body(self.ground_body)

    def update(self):
        self.planet.update()
        self.player.update()
        self.world.Step(self.settings.time_step, 10, 10)

    def exit(self):
        quit()
        sys.exit()

    def run(self):
        while True:
            for evt in event.get():
                # if event.type == WINDOWFOCUSLOST:
                #     self.exit()
                if evt.type == QUIT:
                    self.exit()

                elif evt.type == MOUSEWHEEL:
                    print(evt)
                    print(evt.x, evt.y)
                    self.camera.zoom *= (10 - evt.y)/10


            pressed_keys = key.get_pressed()

            if pressed_keys[K_ESCAPE]:
                self.exit()

            self.update()

            direction: b2Vec2 = (self.planet.get_position() - self.player.get_position())


            self.player.body.ApplyForce(self.normalize(direction) * 10, self.player.body.worldCenter, True)
            self.camera.target = self.player.body.position
            self.render()
                        
            display.update()
            self.FramePerSec.tick(self.FPS)

    def normalize(self, vec: b2Vec2):
        tot = Math.sqrt(vec.x*vec.x + vec.y*vec.y)
        return b2Vec2(vec.x / tot, vec.y / tot)