import pygame
import math


orange = (255, 215, 0)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)
pink = (255, 192, 203)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
blue = (0, 0, 255)
purple = (128, 0, 128)


class Scoreboard():

    current_player = None
    previous_time = None
    step_number = None
    p1_col = None
    p2_col = None
    sound = None

    def __init__(self, current_player):
        self.current_player = current_player
        self.previous_time = pygame.time.get_ticks()
        self.step_number = 1
        self.sound = pygame.mixer.Sound("Game_hit.mp3")

    def is_player_1(self):
        return self.current_player == 1

    def miss(self):
        self.step_number = 1

    def hit(self, health):
        self.sound.play()

        self.step_number = 1

        health = health - 1
        return health

    def draw(self, screen, p1_health, p2_health, p1_col, p2_col, projectile):

        if p1_col == 1:
            self.p1_col = pink
        elif p1_col == 2:
            self.p1_col = red
        elif p1_col == 3:
            self.p1_col = orange
        elif p1_col == 4:
            self.p1_col = yellow
        elif p1_col == 5:
            self.p1_col = green
        elif p1_col == 6:
            self.p1_col = cyan
        elif p1_col == 7:
            self.p1_col = blue
        else:
            self.p1_col = purple

        if p2_col == 1:
            self.p2_col = pink
        elif p2_col == 2:
            self.p2_col = red
        elif p2_col == 3:
            self.p2_col = orange
        elif p2_col == 4:
            self.p2_col = yellow
        elif p2_col == 5:
            self.p2_col = green
        elif p2_col == 6:
            self.p2_col = cyan
        elif p2_col == 7:
            self.p2_col = blue
        else:
            self.p2_col = purple

        p1_img = pygame.image.load('player1.png')
        p2_img = pygame.image.load('player2.png')
        health_img = pygame.image.load('health.png')

        pygame.draw.rect(screen, orange, pygame.Rect(0, 720, 1200, 80))

        # Drawing the current player
        if self.current_player == 1:
            pygame.draw.rect(screen, self.p1_col, pygame.Rect(20, 730, 100, 60))
            screen.blit(p1_img, (25, 745))
        else:
            pygame.draw.rect(screen, self.p2_col, pygame.Rect(1080, 730, 100, 60))
            screen.blit(p2_img, (1085, 745))

        screen.blit(health_img, (215, 765))
        screen.blit(health_img, (895, 765))

        # Drawing the health
        if p1_health == 2:
            pygame.draw.rect(screen, red, pygame.Rect(200, 725, 120, 40))
            screen.blit(health_img, (215, 765))
        elif p1_health == 1:
            pygame.draw.rect(screen, black, pygame.Rect(200, 725, 120, 40))
            pygame.draw.rect(screen, red, pygame.Rect(200, 725, 60, 40))
        else:
            pygame.draw.rect(screen, black, pygame.Rect(200, 725, 120, 40))

        if p2_health == 2:
            pygame.draw.rect(screen, red, pygame.Rect(880, 725, 120, 40))
            screen.blit(health_img, (895, 765))
        elif p2_health == 1:
            pygame.draw.rect(screen, black, pygame.Rect(880, 725, 120, 40))
            pygame.draw.rect(screen, red, pygame.Rect(880, 725, 60, 40))
        else:
            pygame.draw.rect(screen, black, pygame.Rect(880, 725, 120, 40))

        # Drawing the timer
        current_time = pygame.time.get_ticks()

        # If the projectile is not on the screen, the timer can continue to run.
        if projectile == None:
            if current_time - self.previous_time > 200:

                self.previous_time = current_time
                self.step_number = self.step_number + 1

                if self.step_number == 100:
                    return False

        clock = pygame.image.load("clock.png").convert_alpha()
        screen.blit(clock, (565, 725))
        end_x = 600 + math.sin(math.pi / 100 * self.step_number) * 35
        end_y = 760 - math.cos(math.pi / 100 * self.step_number) * 35
        pygame.draw.line(screen, red, (600, 760), (end_x, end_y))

