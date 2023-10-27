import pygame as pg
from pygame.sprite import Sprite
from pygame.math import Vector2 as vec
import os
from settings import *

# setup asset folders here - images sounds etc.
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
snd_folder = os.path.join(game_folder, 'sounds')

class Player(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        # self.image = pg.Surface((50, 50))
        # self.image.fill(GREEN)
        # use an image for player sprite...
        self.game = game
        self.image = pg.image.load(os.path.join(img_folder, 'theBell.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.jumping = False
    def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE] and self.game.jumps > 0 and not self.jumping:
            self.game.jumps -= 1
            self.jumping = True
            self.jump()
        if not keys[pg.K_SPACE]:
            self.jumping = False
    def jump(self):
        hits = pg.sprite.spritecollide(self, self.game.ground, False)
        if hits:
            print("i can jump")
            self.vel.y = -PLAYER_JUMP
    def update(self):
        self.acc = vec(0,PLAYER_GRAV)
        self.controls()

        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos

# platforms

class Cloud(Sprite):
    def __init__(self, x, y, w, h, speed):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 0
        self.speed = speed

    def update(self):
        self.rect.x -= self.speed

class Ground(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 0
        self.speed = 5

    def update(self):
        pass

class Target(Sprite):
    def __init__(self, x, y, w, h, vel, kind):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(D62628)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.kind = kind
        self.pos = vec(x, y)
        self.vel = vec(vel,0)

    def update(self):
        if self.pos.x < 0:
            self.kill()
        
        self.pos += self.vel
        self.rect.midbottom = self.pos
        