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
    
    @nFrames.setter
    def nFrames(self, value):
        self._nFrames = value
    
    @property
    def limit(self):
        return self._limit
    
    @limit.setter
    def limit(self, value):
        self._limit = value