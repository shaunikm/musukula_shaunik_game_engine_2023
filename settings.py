# This file was created by: Chris Cozort
# Content from Chris Bradfield; Kids Can Code
# KidsCanCode - Game Development with Pygame video series
# Video link: https://youtu.be/OmlQ0XCvIn0 
import random

# game settings 
WIDTH = 1024
HEIGHT = 768
FPS = 30

# player settings
PLAYER_JUMP = 25
PLAYER_GRAV = 1.5
global PLAYER_FRIC
PLAYER_FRIC = 0.2

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SKYBLUE = (150, 200, 255)
D62628 = (214, 40, 40)
FCBF49 = (252, 191, 73)
F77F00 = (247, 127, 0)

CLOUD_LIST = [(60, 40), (50, 40), (30, 20)]