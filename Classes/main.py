import cv2
import sys
import pygame
from pigeon import Pigeon
from detection import Detector
from player import Player
from mecanic import Mecanic
from frames import FramesManager

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
        self._framesManager = FramesManager()

    def run(self):
        #O código pode ser melhorado criando um método da classe Game para os ifs de status da detecção
        #e de checagem do loss.
        #Além disso, pode ser criado outro método chamado wait quit, que fica esperando o usuário fechar 
        # o jogo
        Mecanic.spawn_pigeon(self._pigeon)

        while self._player.is_alive():
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

            status, frame = self._videoCapture.read()

            if not status:
                print("Error: Could not read from camera")
                sys.exit(1)

            statusDetection, frameDetected = self._detector.detect(frame)
            image = Mecanic.preprocess_frames(frameDetected)

            if statusDetection:
                Mecanic.hit(self._pigeon, self._detector, self._player, self._framesManager)
            
            if Mecanic.check_loss(self._framesManager):
                self._player.loss()
                self._framesManager.reset()
                Mecanic.spawn_pigeon(self._pigeon)
            else:
                self._framesManager.frameIncrement()
            
            #It is necessary to recalculate the coordinates of the pigeon with respect to the image, because the x axis is inverted
            pigeonCoordinates = (self._screenSize[0] - self._pigeon.position[0], self._pigeon.position[1])
            Mecanic.redirect_the_pigeon(self._pigeon, self._screenSize)

            self._screen.blit(image, (0, 0))
            self._screen.blit(self._pigeon.image, pigeonCoordinates)
            self._screen.blit(self._render_text("Score: " + str(self._player.score), (255, 255, 255)), (0, 0))
            self._screen.blit(self._render_text("Helth: " + str(self._player.health), (255, 255, 255)), (0, 25))

            self._pigeon.move()

            pygame.display.update()
        
        self._videoCapture.release()
        cv2.destroyAllWindows()

        print("You Lose")

    def _render_text(self, text, color):
        return self._systemFont.render(text, True, color)

if __name__ == "__main__":
    main = Game()
    main.run()



