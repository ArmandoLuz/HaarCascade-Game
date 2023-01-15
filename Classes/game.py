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
        self._systemFont = pygame.font.SysFont("pottisreeramulu", 20)
        self._screenSize = (640, 480)
        self._screen = pygame.display.set_mode(self._screenSize)
        self._pigeon = Pigeon()
        self._detector = Detector()
        self._player = Player()
        self._videoCapture = cv2.VideoCapture(0)
        self._framesManager = FramesManager()
        self._background = pygame.image.load("../Assets/background.png")

    def run(self):
        self.menu()

    def menu(self):
        show_options = True
        counter = 0

        while counter <= 128:
            self._get_option()
            self._screen.blit(self._background, (0, 0))
            if counter == 128:
                counter = 0
                show_options = not show_options
            else:
                counter += 1
                
            if show_options:
                self._screen.blit(self._render_text(
                    "Press Space to start", 
                    (255, 255, 255)), 
                    (int(self._screenSize[0]/2) - 60, int(self._screenSize[1]/2) + 130))
                
                self._screen.blit(
                    self._render_text("Last Score: " + str(self._player.score), 
                    (255, 255, 255)), 
                    (int(self._screenSize[0]/2) - 28, int(self._screenSize[1]/2) + 150)
                    )

            pygame.display.update()
    
    def start(self):
        self._player.reset()
        Mecanic.spawn_pigeon(self._pigeon)

        while self._player.is_alive():
            self._wait_quit()

            status, frame = self._videoCapture.read()
            self._check_video(status)
            self._detector.detect(frame)
            self._mecanic_manager()
            
            #It is necessary to recalculate the coordinates of the pigeon with respect to the image, because the x axis is inverted
            pigeonCoordinates = (self._fix_x_axis(self._pigeon.position[0]), self._pigeon.position[1])
            
            self._screen.blit(self._preprocess_frames(self._detector.imageDetected), (0, 0))
            self._screen.blit(self._pigeon.image, pigeonCoordinates)
            self._screen.blit(self._render_text("Score: " + str(self._player.score), (255, 255, 255)), (0, 0))
            self._screen.blit(self._render_text("Helth: " + str(self._player.health), (255, 255, 255)), (0, 25))
            self._screen.blit(self._render_text("Level: " + str(self._player.level), (255, 255, 255)), (0, 50))

            self._pigeon.move()

            pygame.display.update()
        
        self.menu()

    def _render_text(self, text, color):
        return self._systemFont.render(text, True, color)
    
    def _fix_x_axis(self, xAxis):
        return self._screenSize[0] - xAxis
    
    def _wait_quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

    def _preprocess_frames(self, frame):
        surface = pygame.surfarray.make_surface(frame)
        return pygame.transform.rotate(surface, 270)
    
    def _mecanic_manager(self):
        if self._detector.statusDetection:
            Mecanic.hit(self._pigeon, self._detector, self._player, self._framesManager)

        if Mecanic.level_up(self._player):
            self._framesManager.limit_down()
            
        if Mecanic.check_loss(self._framesManager):
            self._player.loss()
            self._framesManager.reset()
            Mecanic.spawn_pigeon(self._pigeon)
        else:
            self._framesManager.frameIncrement()
        
        Mecanic.redirect_the_pigeon(self._pigeon, self._screenSize)

    def _check_video(self, status):
        if not status:
            print("Error: Could not read from camera")
            sys.exit(1)

    def _get_option(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.start()



