import pygame
from pygame.locals import *
import sys, random
import time
pygame.init()
print(pygame.image.get_extended())

# COLORS
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


SPEED = 5
FPS = 60
SCORE = 0
HEIGHT = 600
WIDTH = 400
FRAME_PER_SEC = pygame.time.Clock()
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 100)


font = pygame.font.SysFont('Verdana', 60)
small_font = pygame.font.SysFont('Verdana', 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
    
    def move(self, speed):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-speed, 0)
        if self.rect.right < WIDTH - 5:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(speed, 0)
    

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, WIDTH - 30), 10)
    
    def move(self, speed):
        global SCORE
        self.rect.move_ip(0, speed)
        if self.rect.bottom > HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(30, WIDTH - 30), 10)
    


dis = pygame.display.set_mode((WIDTH, HEIGHT))
dis.fill(WHITE)
pygame.display.set_caption("Game")
player = Player()
enemy = Enemy()

enemies = pygame.sprite.Group()
enemies.add(enemy)
all_sprite = pygame.sprite.Group()
all_sprite.add(enemy)
all_sprite.add(player)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.2
        if event.type == QUIT: 
            pygame.quit()
            sys.exit()
    FRAME_PER_SEC.tick(60)
    dis.blit(background, (0,0))
    scores = small_font.render(str(SCORE), True, BLACK)
    dis.blit(scores, (10,10))
    for entity in all_sprite:
        dis.blit(entity.image, entity.rect)
        entity.move(SPEED)
    if pygame.sprite.spritecollideany(player, enemies):
        pygame.mixer.Sound('crash.wav').play()
        dis.fill(RED)
        dis.blit(game_over, (35, 250))
        pygame.display.update()
        for entity in all_sprite:
            entity.kill()
        time.sleep(2)
        sys.exit()
    pygame.display.update()
