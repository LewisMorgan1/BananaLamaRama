import pygame
import math

WHITE = (255, 255, 255)
width = 50
height = 50

#  This draws and manages a single player. It loads an image from a file to put onto the coordinates of the sprite.

class Sprite(pygame.sprite.Sprite):
    step_number = 1
    current_player = None
    pos_x = None
    pos_y = None
    angle = 1
    screen = None
    power = 50
    current_player_col = None

    def __init__(self, current_player, pos_x, pos_y, screen, current_player_col):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.current_player = current_player
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.screen = screen
        self.current_player_col = current_player_col

        if current_player == 1:
            self.angle = 45
        else:
            self.angle = 125

    def draw(self):

        # Draws a sprite over the top of the rectangle.

        self.image = pygame.image.load("llama_walk" + str(self.step_number)
                                       + "-" + str(self.current_player_col) + ".png").convert_alpha()

        #  Draw the aiming indicator above the sprite, by drawing 10 circles

        if self.current_player == 1:

            for n in range(10):
                #  This is how the power influences the size of the indicator
                line_length = n * (self.power / 10)
                end_pos = (self.pos_x + 60 + (line_length * math.cos(math.radians(self.angle))),
                           self.pos_y + 10 - (line_length * math.sin(math.radians(self.angle))))
                pygame.draw.circle(self.screen, WHITE, end_pos, 3)

        else:

            for n in range(10):
                #  This is how the power influences the size of the indicator
                line_length = n * (self.power / 10)
                end_pos = (self.pos_x + 10 + (line_length * math.cos(math.radians(self.angle))),
                           self.pos_y + 10 - (line_length * math.sin(math.radians(self.angle))))
                pygame.draw.circle(self.screen, WHITE, end_pos, 3)

        if self.current_player == 2:
            image_copy = self.image.copy()
            self.image = pygame.transform.flip(image_copy, True, False)

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y


    def move_left(self):
        #  This makes sure the sprite isn't at lower boundary, which changes based on the player.

        if self.current_player == 1:
            lower_boundary = -10
        else:
            lower_boundary = 980

        if self.pos_x > lower_boundary:
            self.pos_x = self.pos_x - 2
            self.step_number = self.step_number - 1

        if self.step_number == 0:
            self.step_number = 4

        self.draw()

    def move_right(self):
        #  This makes sure the sprite isn't at the upper boundary, which changes based on the player.
        if self.current_player == 1:
            upper_boundary = 140
        else:
            upper_boundary = 1140

        if self.pos_x < upper_boundary:
            self.pos_x = self.pos_x + 2
            self.step_number = self.step_number + 1

        if self.step_number == 5:
            self.step_number = 1

        self.draw()

    def increase_angle(self):
        #  This makes sure the indicator can't face down, as this definity wouldn't work.
        if self.angle < 180:
            self.angle = self.angle + 1

        self.draw()

    def reduce_angle(self):
        #  This makes sure the indicator can't face down, as this definity wouldn't work.
        if self.angle > 0:
            self.angle = self.angle - 1

        self.draw()

    def increase_power(self):
        #  Makes sure the power does go above 100.
        if self.power <= 100:
            self.power = self.power + 2


    def reduce_power(self):
        #  Makes sure power does go below 10.
        if self.power >= 10:
            self.power = self.power - 2

    def get_pos_x(self):
        return self.pos_x

    def get_pos_y(self):
        return self.pos_y

    def get_power(self):
        return self.power

    def get_angle(self):
        return self.angle

    def is_collision(self, pos_x, pos_y):
        #  Checks if the position of the projectile passed in are within range of the opponent sprite.
        if pos_x < self.pos_x + 70 and pos_x > self.pos_x and pos_y < self.pos_y + 40 and pos_y > self.pos_y + 10:
            return True
        else:
            return False

