
from dataclasses import dataclass
import json

from singleton import Singleton

@dataclass(frozen=True)
class Settings(metaclass=Singleton):
    window_caption: str = "gaminator"
    screen_width: int = 800
    screen_height: int = 800
    fps: int = 60
    ppm: float = 20.0  # pixels per meter
    time_step: float = 1.0 / fps


    def __init__(self):
        pass
