import pygame

screen_width = 500
screen_height = 400
game_width = 16
game_height = 12
mines = 40
size_square = 20
bugx = 100
bugy = 365

iconfile = pygame.image.load('images/flag.png')
square = pygame.image.load('images/square.png')
square_pressed = pygame.image.load('images/square_pressed.png')
mine = pygame.image.load('images/mine.png')
flag = pygame.image.load('images/flag.png')
one = pygame.image.load('images/1.png')
two = pygame.image.load('images/2.png')
three = pygame.image.load('images/3.png')
four = pygame.image.load('images/4.png')
five = pygame.image.load('images/5.png')
six = pygame.image.load('images/6.png')
seven = pygame.image.load('images/7.png')
eight = pygame.image.load('images/8.png')
background = pygame.image.load('images/background.png')
bug1 = pygame.image.load('images/bug1.png')
bug2 = pygame.image.load('images/bug2.png')
bug3 = pygame.image.load('images/bug3.png')
bug4 = pygame.image.load('images/bug2.png')

class MouseButtons:
    LEFT = 1
    MIDDLE = 2
    RIGHT = 3
    WHEEL_UP = 4
    WHEEL_DOWN = 5



