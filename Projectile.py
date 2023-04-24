import pygame
import math

gravity = 9.81

transparent = (0,0,0,0)
#This class draws an image when fire_projectile calls it.
class Projectile(pygame.sprite.Sprite):
    pos_x = None
    initial_pos_x = None
    initial_pos_y = None
    pos_y = None
    previous_time = None
    power = None
    angle = None
    time = 0
    sound = None

    def __init__(self, x, y, power, angle):
        super().__init__()
        self.pos_x = x
        self.pos_y = y
        self.initial_pos_x = x
        self.initial_pos_y = y
        self.power = power
        self.angle = angle
        self.previous_time = pygame.time.get_ticks()
        self.sound = pygame.mixer.Sound("Game_bullet.mp3")



    def draw(self, screen):

        self.sound.play()

        # Loads the projectile image
        self.image = pygame.image.load("banana.png").convert_alpha()
        #Draws the projectile using the image and pos_x and pos_y variables.
        screen.blit(self.image, (self.pos_x, self.pos_y))

        current_time = pygame.time.get_ticks()

        vx = self.power * math.cos(math.radians(self.angle)) # velocity in the x direction
        vy = self.power * math.sin(math.radians(self.angle)) # velocity in the y direction


        if current_time - self.previous_time > 5:

            self.previous_time = current_time
            # Calculates the x position of the projectile using this formula
            self.pos_x = self.initial_pos_x + vx * self.time
            # Calculates the y position of the projectile using this formula
            self.pos_y = self.initial_pos_y - (vy * self.time - 0.5 * gravity * self.time ** 2)



            self.time = self.time + 0.1


    def get_pos_x(self):
        return self.pos_x

    def get_pos_y(self):
        return self.pos_y

