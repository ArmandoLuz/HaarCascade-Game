import cv2
import sys
import pygame
from pigeon import Pigeon
from detection import Detector
from player import Player
from mecanic import Mecanic

class Game:
    def __init__(self):
        pygame.init()
        self._systemFont = pygame.font.SysFont(pygame.font.get_default_font(), 25)
        self._screenSize = (640, 480)
        self._screen = pygame.display.set_mode(self._screenSize)
        self._pigeon = Pigeon()
        self._detector = Detector()
        self._player = Player()
        self._videoCapture = cv2.VideoCapture(0)

    def run(self):
        self._pigeon.spawn()

        while self._player.isAlive():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

            status, frame = self._videoCapture.read()

            if not status:
                print("Error: Could not read from camera")
                sys.exit(1)

            statusDetection, frameDetected = self._detector.detect(frame)

            if statusDetection:
                Mecanic.hit(self._pigeon, self._detector, self._player)

            surface = pygame.surfarray.make_surface(frameDetected)
            image = pygame.transform.rotate(surface, 270)
            
            #It is necessary to recalculate the coordinates of the pigeon with respect to the image, because the x axis is inverted
            pigeonCoordinates = (self._screenSize[0] - self._pigeon.position[0], self._pigeon.position[1])
            Mecanic.redirect_the_pigeon(self._pigeon, self._screenSize)

            self._screen.blit(image, (0, 0))
            self._screen.blit(self._pigeon.image, pigeonCoordinates)
            self._screen.blit(self._get_score(), (0, 0))

            self._pigeon.move()

            pygame.display.update()
        
        self._videoCapture.release()
        cv2.destroyAllWindows()

    def _get_score(self):
        return self._systemFont.render("Score: " + str(self._player.score), True, (255, 255, 255))

if __name__ == "__main__":
    main = Game()
    main.run()



