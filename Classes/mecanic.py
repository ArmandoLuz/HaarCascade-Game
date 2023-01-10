from pigeon import Pigeon
from detection import Detector
from player import Player

class Mecanic:
    
    @classmethod
    def hit(cls, pigeon, hand, player):
        if isinstance(pigeon, Pigeon) and isinstance(hand, Detector) and isinstance(player, Player):
            if cls._check_xAxis(pigeon, hand) and cls._check_yAxis(pigeon, hand):
                player.hit()
                print("Score: " + str(player.score))
                pigeon.spawn()
                return True
            else:
                return False
        else:
            print("Error: Invalid type of object")
    
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
        if isinstance(pigeon, Pigeon):
            if pigeon.position[0] < 0:
                pigeon.position[0] = screenSize[0]
            elif pigeon.position[0] > screenSize[0]:
                pigeon.position[0] = 0

            if pigeon.position[1] < 0:
                pigeon.position[1] = screenSize[1]
            elif pigeon.position[1] > screenSize[1]:
                pigeon.position[1] = 0
        else:
            print("Error: Invalid type of object")

