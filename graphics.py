import os
from utilities import*

pygame.init()
pygame.display.set_icon(iconfile)
pygame.display.set_caption('Minesweeper')
gameDisplay = pygame.display.set_mode((screen_width,screen_height))

w, h = pygame.display.Info().current_w, pygame.display.Info().current_h
w = w/3.3
h = h/4
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (w,h)

clock = pygame.time.Clock()

def printimg (image , x , y ) :
    gameDisplay.blit(image, (x, y))
