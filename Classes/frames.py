class FramesManager:

    def __init__(self):
        self._nFrames = 0
        self._limit = 32

    def reset(self):
        self._nFrames = 0
    
    def frameIncrement(self):
        self._nFrames += 1
    
    @property
    def nFrames(self):
        return self._nFrames
    
    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, limit):
        self._limit = limit
