import pygame

class Mecanic:
    
    @classmethod
    def hit(cls, pigeon, hand, player, frames):
        if cls._check_xAxis(pigeon, hand) and cls._check_yAxis(pigeon, hand):
            player.hit()
            frames.reset()
            cls.spawn_pigeon(pigeon)
            return True
        else:
            return False
    
    @classmethod
    def _check_xAxis(cls, pigeon, hand):
        if pigeon.position[0] >= hand.coordinates["xAxisInit"] and pigeon.position[0] <= hand.coordinates["xAxisEnd"]:        
            return True
        else:
            return False
    
    @classmethod
    def _check_yAxis(cls, pigeon, hand):
        if pigeon.position[1] >= hand.coordinates["yAxisInit"] and pigeon.position[1] <= hand.coordinates["yAxisEnd"]:
            return True
        else:
            return False

    @classmethod
    def redirect_the_pigeon(cls, pigeon, screenSize):
        if pigeon.position[0] < 0:
            pigeon.position[0] = screenSize[0]
        elif pigeon.position[0] > screenSize[0]:
            pigeon.position[0] = 0

        if pigeon.position[1] < 0:
            pigeon.position[1] = screenSize[1]
        elif pigeon.position[1] > screenSize[1]:
            pigeon.position[1] = 0

    @classmethod
    def spawn_pigeon(cls, pigeon):
        pigeon.spawn()

    @classmethod
    def check_loss(cls, frames):
        if frames.nFrames >= frames.limit:
            return True
        else:
            return False

    @classmethod
    def level_up(self, player):
        if player.score >= player.level * 10:
            return True
        else:
            return False


