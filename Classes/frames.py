class FramesManager:

    def __init__(self):
        self._nFrames = 0
        self._limit = 80

    def reset(self):
        self._nFrames = 0
    
    def frameIncrement(self):
        self._nFrames += 1

    def limit_down(self):
        if self._limit > 8:
            self._limit -= 8
    
    @property
    def nFrames(self):
        return self._nFrames
    
    @property
    def limit(self):
        return self._limit


