class Player:
    def __init__(self):
        self._health = 100
        self._score = 0
    
    def hit(self):
        self._score += 1
    
    def loss(self):
        self._health -= 10
    
    def isDead(self):
        return True if self._health <= 0 else False
    
    def isAlive(self):
        return True if self._health > 0 else False
    
    @property
    def health(self):
        return self._health
    
    @property
    def score(self):
        return self._score

    @health.setter
    def health(self, health):
        self._health = health
    
    @score.setter
    def score(self, score):
        self._score = score
    