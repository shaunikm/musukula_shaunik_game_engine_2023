# game settings 
WIDTH = 360
HEIGHT = 480
FPS = 30
SCORE = 0

# player settings
PLAYER_JUMP = 20
PLAYER_GRAV = 1.5

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

# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, " "),
                 (WIDTH / 2 - 25, HEIGHT * 3 / 4, 100, 20, " "),
                 (125, HEIGHT - 300, 100, 20, "moving"),
                 (200, HEIGHT - 200, 100, 20, "moving"),
                 (175, 100, 50, 20, " ")]