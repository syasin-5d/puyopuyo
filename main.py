import pygame
from pygame.locals import *
import sys

WIDTH, HEIGHT = 640, 480
FPS = 30
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Main:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.clock.tick(FPS)

    def MainLoop(self):
        x, y = 100, 200
        pygame.key.set_repeat(200, 40)
        rect = pygame.Rect((x, y), (32, 32))
        image = pygame.Surface((32, 32))
        image.fill(WHITE)
        while True:
            # rect = pygame.draw.rect(self.screen, (0, 80, 0),
            #                         Rect(x, y, 50, 50), 5)
            pygame.time.wait(30)
            for event in pygame.event.get():
                mods = pygame.key.get_mods()
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE or (
                            mods & KMOD_CTRL
                            and event.key == K_c) or event.key == K_q:
                        pygame.quit()
                        sys.exit()
                    if event.key == K_h:
                        rect.move_ip(-2, 0)
                    if event.key == K_l:
                        rect.move_ip(2, 0)
                    if event.key == K_k:
                        rect.move_ip(0, -2)
                    if event.key == K_j:
                        rect.move_ip(0, 2)
            self.screen.fill(BLACK)
            self.screen.blit(image, rect)
            pygame.display.update()


def main():
    main_window = Main(WIDTH, HEIGHT)
    main_window.MainLoop()


if __name__ == "__main__":
    main()
