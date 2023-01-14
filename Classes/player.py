class Player:
    def __init__(self):
        self._health = 100
        self._score = 0
        self._level = 1
    
    def hit(self):
        self._score += 1
    
    def loss(self):
        self._health -= 10
    
    def is_dead(self):
        return True if self._health <= 0 else False
    
    def is_alive(self):
        return True if self._health > 0 else False

    def reset(self):
        self._health = 100
        self._level = 1
        self._score = 0
    
    @property
    def health(self):
        return self._health
    
    @property
    def score(self):
        return self._score

    @property
    def level(self):
        return self._level
    
    @level.setter
    def level(self, value):
        self._level = value
    