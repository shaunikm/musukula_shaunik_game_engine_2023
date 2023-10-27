# content from kids can code: http://kidscancode.org/blog/

# GameDesign:
# Goals: Get to the exit at the top of the level
# Rules: Can't hit any mobs
# Feedback: WASD for to move around
# Freedom: moving around

# Feature Goals:
# Have mobs that move around
# Have obstacles that bounce the player backwards from the point of collision

# import libraries and modules
import pygame as pg
from pygame.sprite import Sprite
import random
from random import randint
import os
from settings import *
from sprites import *

vec = pg.math.Vector2

# setup asset folders here - images sounds etc.
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
snd_folder = os.path.join(game_folder, 'sounds')

class Game:
    def __init__(self):
        # init pygame and create a window
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("My Game...")
        self.clock = pg.time.Clock()
        self.running = True
    
    def new(self):
        # create a group for all sprites
        self.jumps = 5 
        self.all_sprites = pg.sprite.Group()
        self.all_clouds = pg.sprite.Group()
        self.ground = pg.sprite.Group()
        self.all_mobs = pg.sprite.Group()
        # instantiate classes
        self.player = Player(self)
        # add instances to groups
        self.all_sprites.add(self.player)

        # instantiation of the Platform class
        ground = Ground(0, HEIGHT - 40, WIDTH, 40)
        self.all_sprites.add(ground)
        self.ground.add(ground)

        for c in range(0, 10):
            cloud = random.choice(CLOUD_LIST)
            c = Cloud(random.randint(0, WIDTH), random.randint(0, HEIGHT-40), cloud[0], cloud[1], 2)
            self.all_sprites.add(c)
            self.all_clouds.add(c)

        for m in range(0,10):
            m = Target(WIDTH, randint(0, HEIGHT), 20, 20, -10, "normal")
            self.all_sprites.add(m)
            self.all_mobs.add(m)

        self.run()
    
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()

        # this is what prevents the player from falling through the platform when falling down...
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.ground, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0

                    
         # this prevents the player from jumping up through a platform
        if self.player.vel.y < 0:
            hits = pg.sprite.spritecollide(self.player, self.ground, False)
            if hits:
                if self.player.rect.bottom >= hits[0].rect.top - 1:
                    self.player.rect.top = hits[0].rect.bottom
                    self.player.acc.y = 5
                    self.player.vel.y = 0

    def events(self):
        for event in pg.event.get():
        # check for closed window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
                
    def draw(self):
        ############ Draw ################
        # draw the background screen
        self.screen.fill(SKYBLUE)
        # draw all sprites
        self.all_sprites.draw(self.screen)
        self.draw_text("Jumps: " + str(self.jumps), 22, WHITE, WIDTH/2, HEIGHT/10)
        # buffer - after drawing everything, flip display
        pg.display.flip()
    
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)

    def show_start_screen(self):
        pass
    def show_go_screen(self):
        pass

g = Game()
while g.running:
    g.new()


pg.quit()
