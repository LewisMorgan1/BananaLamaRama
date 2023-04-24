import pygame
from GameController import GameController
from Map import Map

BLACK = (0, 0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)

class MainMenu():

    carry_on = None
    map_selection = None
    row = None
    p1_col_selection = None
    p2_col_selection = None
    game_controller = None

    def __init__(self, screen):

        self.carry_on = True
        self.screen = screen
        self.previous_time = pygame.time.get_ticks()
        self.step_number = 1
        self.map_selection = 1
        self.row = 1
        self.p1_col_selection = 1
        self.p2_col_selection = 1

    def draw(self):
        carry_on = True
        self.game_controller = GameController(self.screen, 2, 2)

        while carry_on:
            self.redraw()
            pygame.display.update()
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.KEYDOWN:

                    if event.type == pygame.KEYDOWN:

                        if event.key == pygame.K_RETURN:
                            exit()

                        elif event.key == pygame.K_UP:
                            if self.row > 1:
                                 self.row = self.row - 1

                        elif event.key == pygame.K_DOWN:
                            if self.row < 4:
                                self.row = self.row + 1

                    if self.row == 1:

                                if event.key == pygame.K_LEFT:
                                    self.map_selection = self.map_selection - 1
                                    if self.map_selection == 0:
                                        self.map_selection = 5

                                elif event.key == pygame.K_RIGHT:
                                    self.map_selection = self.map_selection + 1
                                    if self.map_selection == 6:
                                        self.map_selection = 1

                    elif self.row == 2:

                        if event.key == pygame.K_LEFT:
                            self.p1_col_selection = self.p1_col_selection - 1
                            if self.p1_col_selection == 0:
                                self.p1_col_selection = 8

                        elif event.key == pygame.K_RIGHT:
                            self.p1_col_selection = self.p1_col_selection + 1
                            if self.p1_col_selection == 9:
                                self.p1_col_selection = 1

                    elif self.row == 3:

                        if event.key == pygame.K_LEFT:
                            self.p2_col_selection = self.p2_col_selection - 1
                            if self.p2_col_selection == 0:
                                self.p2_col_selection = 8

                        elif event.key == pygame.K_RIGHT:
                            self.p2_col_selection = self.p2_col_selection + 1
                            if self.p2_col_selection == 9:
                                self.p2_col_selection = 1

                    elif self.row == 4:

                        if event.key == pygame.K_SPACE:
                            # Starts the game
                            carry_on = False

        done = self.game_controller.start(Map(self.screen, self.map_selection),
                                          self.p1_col_selection, self.p2_col_selection)

        if done:
            # Resets the selections
            self.row = 1
            self.map_selection = 1
            self.p1_col_selection = 1
            self.p2_col_selection = 1
            return True

    def redraw(self):
        pygame.key.set_repeat(0, 50)
        self.screen.fill(BLACK)

        # Changes the text colour when the row is selected.
        if self.row == 1:
            map_text_col = ORANGE
        else:
            map_text_col = WHITE
        if self.row == 2:
            p1_text_col = ORANGE
        else:
            p1_text_col = WHITE
        if self.row == 3:
            p2_text_col = ORANGE
        else:
            p2_text_col = WHITE

        # Draws the unselected white boxes and the selected orange box
        for box_num in range(5):
            pygame.draw.rect(self.screen, WHITE, pygame.Rect((234 * (box_num + 1)) - 184, 100, 150, 100))
        pygame.draw.rect(self.screen, ORANGE, pygame.Rect((234 * self.map_selection) - 184, 100, 150, 100))

        # Draws the map images
        for picture_num in range(5):
            img = pygame.image.load("Map" + str(picture_num + 1) + ".jpeg").convert_alpha()
            picture = pygame.transform.scale(img, (140, 90))
            self.screen.blit(picture, ((234 * (picture_num + 1)) - 179, 105))

        # Font and text size
        font = pygame.font.Font('game_font.ttf', 20)

        # Map text
        for x in range(6):
            text = font.render(("Map" + str(x)), False, map_text_col)
            textRect = text.get_rect()
            textRect.center = ((234 * x) - 104, 210)
            self.screen.blit(text, textRect)

        # Title text
        text = font.render("Banana Llama Rama!", False, ORANGE)
        textRect = text.get_rect()
        textRect.center = (1200 // 2, 40 // 2)
        self.screen.blit(text, textRect)

        # Draws the selected colour wheel
        current_p1_colour = pygame.image.load('col' + str(self.p1_col_selection) + '.png')
        self.screen.blit(current_p1_colour, (475, 200))
        current_p2_colour = pygame.image.load('col' + str(self.p2_col_selection) + '.png')
        self.screen.blit(current_p2_colour, (475, 400))

        # Colour wheel caption
        text = font.render("Player 1 Colour", False, p1_text_col)
        textRect = text.get_rect()
        textRect.center = (1200 // 2, 425)
        self.screen.blit(text, textRect)
        text = font.render("Player 2 Colour", False, p2_text_col)
        textRect = text.get_rect()
        textRect.center = (1200 // 2, 625)
        self.screen.blit(text, textRect)

        # If start button is selected draws box around start button
        if self.row == 4:
            pygame.draw.rect(self.screen, ORANGE, pygame.Rect(540, 665, 120, 70))
        pygame.draw.rect(self.screen, WHITE, pygame.Rect(550, 675, 100, 50, ))
        text = font.render("Start", False, ORANGE)
        textRect = text.get_rect()
        textRect.center = (1200 // 2, 700)
        self.screen.blit(text, textRect)

