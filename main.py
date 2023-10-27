# This file was created by: Shaunik Musukula

# import libraries and modules
import pygame as pg
import random
from random import randint
import os
from settings import *
from sprites import *
from math import floor

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
        self.start = False
        self.dead = False
        self.target_count = TARGET_COUNT
        self.cloud_count = CLOUD_COUNT
    
    def new(self):
        # create a group for all sprites
        self.jumps = 3
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.all_clouds = pg.sprite.Group()
        self.all_targets = pg.sprite.Group()
        # instantiate classes

        for c in range(self.cloud_count):
            cloud = random.choices(CLOUD_LIST, weights=CLOUD_WEIGHTS, k=1)[0]
            c = Cloud(random.randint(0, WIDTH), random.randint(0, HEIGHT-40), cloud, CLOUD_SPEED, self)
            self.all_sprites.add(c)
            self.all_clouds.add(c)
            
        for t in range(self.target_count):
            t = Target(random.randint(WIDTH-WIDTH//3, WIDTH), randint(0, HEIGHT), TARGET_SPEED + 2*self.score**(1/SPEED_FAC), "normal", self)
            self.all_sprites.add(t)
            self.all_targets.add(t)
        
        self.player = Player(self)
        # add instances to groups
        self.all_sprites.add(self.player)

        self.run()
    
    def run(self):
        self.playing = True
        while not self.start:
            self.clock.tick(FPS)
            self.events()
            self.show_start_screen()
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            if not self.dead:
                self.update()
                self.draw()
            elif self.dead:
                self.show_end_screen()

    def new_target(self):
        t = Target(WIDTH, randint(0, HEIGHT), TARGET_SPEED + 2*self.score**(1/SPEED_FAC), "normal", self)
        self.all_sprites.add(t)
        self.all_targets.add(t)
        self.target_count += 1
    
    def new_cloud(self):
        cloud = random.choices(CLOUD_LIST, weights=CLOUD_WEIGHTS, k=1)[0]
        c = Cloud(WIDTH, random.randint(0, HEIGHT-40), cloud, CLOUD_SPEED, self)
        self.all_sprites.add(c)
        self.all_clouds.add(c)
        self.cloud_count += 1
    
    def update(self):
        self.all_sprites.update()
        self.score += SCORE_INC
        
        thits = pg.sprite.spritecollide(self.player, self.all_targets, False)
        if thits:
            self.jumps += 1
            thits[0].die()
            
        if self.cloud_count < CLOUD_COUNT: self.new_cloud()
        if self.target_count < TARGET_COUNT: self.new_target()

    def events(self):
        for event in pg.event.get():
        # check for closed window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
                self.start = True
                
    def draw(self):
        ############ Draw ################
        # draw the background screen
        self.screen.fill(SKYBLUE)
        # draw all sprites
        self.all_sprites.draw(self.screen)
        self.draw_text("Jumps: " + str(self.jumps), FONT_SIZE, BLACK, WIDTH/2, HEIGHT/10)
        self.draw_text("Score: " + str(floor(self.score)), FONT_SIZE, BLACK, WIDTH/2, HEIGHT/10+SPACING)
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
        self.screen.fill(SKYBLUE)
        self.draw_text("Press -enter- to start", FONT_SIZE, BLACK, WIDTH/2, HEIGHT/2)
        keys = pg.key.get_pressed()
        if keys[pg.K_RETURN]:
            self.start = True
        pg.display.flip()

    def show_end_screen(self):
        self.draw_text("You died :(", FONT_SIZE, BLACK, WIDTH/2, HEIGHT/2)
        self.draw_text("Press -enter- to retry", FONT_SIZE, BLACK, WIDTH/2, HEIGHT/2+SPACING)
        keys = pg.key.get_pressed()
        if keys[pg.K_RETURN]:
            self.dead = False
            self.new()
        pg.display.flip()

g = Game()
while g.running:
    g.new()


pg.quit()
