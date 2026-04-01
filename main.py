import pygame
from pygame.locals import *
import sys, random
pygame.init()
print(pygame.image.get_extended())

# COLORS
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


FPS = 60
HEIGHT = 800
WIDTH = 800
FRAME_PER_SEC = pygame.time.Clock()
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
    
    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < WIDTH - 5:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)

dis = pygame.display.set_mode((WIDTH, HEIGHT))
dis.fill(WHITE)
player = Player()

while True:
    for event in pygame.event.get():
        if event.type == QUIT: 
            pygame.quit()
            sys.exit()
    FRAME_PER_SEC.tick(60)
    dis.fill(WHITE)
    player.draw(dis)
    player.update()
    pygame.display.update()
