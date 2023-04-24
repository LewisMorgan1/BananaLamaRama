import pygame

from MainMenu import MainMenu

pygame.init()
pygame.key.set_repeat(1, 50)

# Constants declaration
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
SCREENWIDTH = 1200
SCREENHEIGHT = 800
FRAMES_PER_SECOND = 60

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Banana Llama Rama!")

carry_on = True

mainMenu = MainMenu(screen)
while carry_on:
    carry_on = mainMenu.draw()

pygame.quit()

