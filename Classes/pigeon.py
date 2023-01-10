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
        xAxis = (np.random.randint(self._position[0] - 20, self._position[0] + 20))
        yAxis = (np.random.randint(self._position[1] - 20, self._position[1] + 20))
        self._position = [xAxis, yAxis]
        return self.position

    @property
    def image(self):
        return self._image
    
    @image.setter
    def image(self, image):
        self._image = image

    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, position):
        self._position = position

    @property
    def dimensions(self):
        return self._dimensions
    
    @dimensions.setter
    def dimensions(self, dimensions):
        self._dimensions = dimensions