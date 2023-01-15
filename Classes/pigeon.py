import numpy as np
from pygame import image

class Pigeon:
    def __init__(self):
        self._image = image.load("../Assets/pigeon.png")
        self._dimensions = self._image.get_size()
        self._position = self._dimensions
    
    def spawn(self):
        randomPoint = np.random.randint(35, 450)
        self._position = [randomPoint, randomPoint]
        return self._position

    def move(self):
        xAxis = np.random.randint(self._position[0] - 15, self._position[0] + 15)
        yAxis = np.random.randint(self._position[1] - 15, self._position[1] + 15)
        self._position = [xAxis, yAxis]
        return self.position

    @property
    def image(self):
        return self._image

    @property
    def position(self):
        return self._position

    @property
    def dimensions(self):
        return self._dimensions