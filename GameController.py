import pygame
from Sprite import Sprite
from Scoreboard import Scoreboard
from Projectile import Projectile
from EndScreen import EndScreen
#from MainMenu import MainMenu


#Constants declaration
BLACK = (0, 0, 0)
FRAMES_PER_SECOND = 100


# The overall controller for the game. It sets up the sprites, map, scoreboard and tells them to draw themselves.
# It then waits for keyboard input to call the appropriate method.
class GameController():
    screen = None             # Pygame object used to draw with
    map = None                # Mountain map
    difficulty_level = 1      # 1 = Beginner, 2 = Intermediate, 3 = Advanced.
    player_1 = None           # Object for left player
    player_2 = None           # Object for right player
    scoreboard = None
    pos_x = None
    pos_y = None
    angle = None
    power = None
    projectile = None
    timer_done = None
    end_screen = None
    main_menu = None
    sound = None
    previous_time = None
    p1_current_health = None
    p2_current_health = None
    p1_col = None
    p2_col = None



    def __init__(self, screen, p1_current_health, p2_current_health):
        self.screen = screen
        self.p1_current_health = p1_current_health
        self.p2_current_health = p2_current_health
        # Add the code for this
        self.sound = pygame.mixer.Sound("explosion_sound.mp3")

    #This method sets up the game.
    #
    #:param the_map: current selected map from menu
    #:param player_1_colour: colour represented as an RGB
    #:param player_2_colour: colour represented as an RGB
    #:param difficulty: difficulty selected from menu

    def start(self, the_map, player_1_colour, player_2_colour):
        self.p1_col = player_1_colour
        self.p2_col = player_2_colour
        self.map = the_map
        self.scoreboard = Scoreboard(1)
        self.end_screen = EndScreen(self.screen)



        # Creates list of pygame sprites
        all_sprites_list = pygame.sprite.Group()
        # Create and add sprites to the list
        self.player_1 = Sprite(1, 50, 632, self.screen, self.p1_col)
        self.player_2 = Sprite(2, 1100, 632, self.screen, self.p2_col)
        self.player_1.draw()
        self.player_2.draw()

        pygame.key.set_repeat(1, 50)

        all_sprites_list.add(self.player_1)
        all_sprites_list.add(self.player_2)

        carry_on = True
        done = True
        clock = pygame.time.Clock()

        while carry_on:
            self.screen.fill(BLACK)


            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        exit()

                    # When left key is pressed and the projectile is not being fired.
                    elif event.key == pygame.K_LEFT and self.projectile == None:
                        if self.scoreboard.is_player_1():
                            self.player_1.move_left()
                        else:
                            self.player_2.move_left()

                    # When right key is pressed and the projectile is not being fired.
                    elif event.key == pygame.K_RIGHT and self.projectile == None:
                        if self.scoreboard.is_player_1():
                            self.player_1.move_right()
                        else:
                            self.player_2.move_right()

                    # When 'a' key is pressed and the projectile is not being fired.
                    elif event.key == pygame.K_a and self.projectile == None:
                        if self.scoreboard.is_player_1():
                            self.player_1.increase_angle()
                        else:
                            self.player_2.increase_angle()

                    # When 'd' key is pressed and the projectile is not being fired.
                    elif event.key == pygame.K_d and self.projectile == None:
                        if self.scoreboard.is_player_1():
                            self.player_1.reduce_angle()
                        else:
                            self.player_2.reduce_angle()

                    # When 'w' key is pressed and the projectile is not being fired.
                    elif event.key == pygame.K_w and self.projectile == None:
                        if self.scoreboard.is_player_1():
                            self.player_1.increase_power()
                        else:
                            self.player_2.increase_power()

                    # When 's' key is pressed and the projectile is not being fired.
                    elif event.key == pygame.K_s and self.projectile == None:
                        if self.scoreboard.is_player_1():
                            self.player_1.reduce_power()
                        else:
                            self.player_2.reduce_power()

                    # When space key is pressed and the projectile is not being fired.
                    elif event.key == pygame.K_SPACE and self.projectile == None:
                        self.fire_projectile()


            self.player_1.draw()
            self.player_2.draw()

            if self.projectile != None: # If projectile is being fired
                self.projectile.draw(self.screen)
                if self.map.is_collision(self.projectile.get_pos_x(), self.projectile.get_pos_y()):
                    # Collision with map
                    self.scoreboard.miss()
                    self.projectile = None

                    # Swaps the current player when the projectile hits something.
                    self.swap_player()

                elif self.scoreboard.is_player_1():
                    if self.player_2.is_collision(self.projectile.get_pos_x(), self.projectile.get_pos_y()):

                        # Collision with other player

                        new_health = self.scoreboard.hit(self.p2_current_health)
                        self.p2_current_health = new_health


                        self.projectile = None

                        # Swaps the current player when the projectile hits something.
                        self.swap_player()

                else:
                    if self.player_1.is_collision(self.projectile.get_pos_x(), self.projectile.get_pos_y()):
                        # Collision with other player

                        new_health = self.scoreboard.hit(self.p1_current_health)
                        self.p1_current_health = new_health

                        self.projectile = None

                        self.swap_player()

            #Draws the sprites
            all_sprites_list.draw(self.screen)
            self.map.draw()
            self.timer_done = self.scoreboard.draw(self.screen, self.p1_current_health, self.p2_current_health,
                                                   self.p1_col, self.p2_col, self.projectile)

            if self.p2_current_health == 0 or self.p1_current_health == 0:
                done = False

            if self.timer_done == False:

                # Swaps the current player when the timer runs out.

                self.swap_player()

            pygame.display.update()
            clock.tick(FRAMES_PER_SECOND)

            # Draw End Screen
            while done == False:
                if self.p1_current_health == 0:
                    menu = self.end_screen.draw(str(2))
                else:
                    menu = self.end_screen.draw(str(1))

                if menu:
                    return True
                    done = True
                    carry_on = False


# This method draws the projectile along a trajectory until it collides with the map or a sprite.
    def fire_projectile(self):
        # Gets the appropriate variables from the sprite class.
        if self.scoreboard.is_player_1():
            self.pos_x = self.player_1.get_pos_x() + 60
            self.pos_y = self.player_1.get_pos_y()
            self.power = self.player_1.get_power() * 1.2
            self.angle = self.player_1.get_angle()
        else:
            self.pos_x = self.player_2.get_pos_x()
            self.pos_y = self.player_2.get_pos_y()
            self.power = self.player_2.get_power() * 1.2
            self.angle = self.player_2.get_angle()
        self.projectile = Projectile(self.pos_x, self.pos_y, self.power, self.angle)

    # Swaps the current player when the projectile hits something.
    def swap_player(self):
        if self.scoreboard.is_player_1():
            self.scoreboard = Scoreboard(2)
        else:
            self.scoreboard = Scoreboard(1)










