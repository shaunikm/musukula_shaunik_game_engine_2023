# This file was created by: Shaunik Musukula

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
        self.image = pg.image.load(os.path.join(img_folder, 'flyer.png')).convert()
        self.image.set_colorkey(BLACK)
        self.image = pg.transform.scale(self.image, (self.image.get_width() * 0.5, self.image.get_height() * 0.5))
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)
        self.pos = vec(WIDTH/3, HEIGHT/2)
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
        self.vel.y = -PLAYER_JUMP
    def update(self):
        self.acc = vec(0,PLAYER_GRAV)
        self.controls()

        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos
        
        if self.rect.top > HEIGHT:
            self.game.dead = True
        self.zorder = 1

class Cloud(Sprite):
    def __init__(self, x, y, type, speed, game):
        Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(img_folder, type)).convert()
        self.image.set_colorkey(BLACK)
        self.image = pg.transform.scale(self.image, (self.image.get_width() * 0.75, self.image.get_height() * 0.75))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 0
        self.speed = speed
        self.game = game

    def update(self):
        self.rect.x -= self.speed
        self.zorder = -1
        if self.rect.right < 0:
            self.die()
            
            
    def die(self):
        self.kill()
        self.game.cloud_count -= 1

class Target(Sprite):
    def __init__(self, x, y, vel, kind, game):
        Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(img_folder, 'jump_arrow.png')).convert()
        self.image.set_colorkey(BLACK)
        self.image = pg.transform.scale(self.image, (self.image.get_width() * 0.75, self.image.get_height() * 0.75))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.kind = kind
        self.pos = vec(x, y)
        self.vel = vec(-vel,0)
        self.game = game

    def update(self):
        if self.rect.right < 0:
            self.die()
        
        self.pos += self.vel
        self.rect.midbottom = self.pos
    
    def die(self):
        self.kill()
        self.game.target_count -= 1
        