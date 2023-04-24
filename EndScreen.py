import pygame

BLACK = (0, 0, 0, 0)
YELLOW = (255, 255, 0)

pygame.font.init()

class EndScreen():

    carry_on = None
    main_menu = None
    menu = None

    def __init__(self, screen):

        self.carry_on = True
        self.screen = screen
        self.previous_time = pygame.time.get_ticks()
        self.step_number = 1
        self.menu = False

    def draw(self, winner):

        self.screen.fill(BLACK)

        while self.carry_on:

            current_time = pygame.time.get_ticks()

            if current_time - self.previous_time > 50:

                self.previous_time = current_time
                self.step_number = self.step_number + 1
                if self.step_number == 34:
                    self.step_number = 1

                img = pygame.image.load("fire_gif_" + str(self.step_number) + ".png").convert_alpha()
                picture = pygame.transform.scale(img, (1200, 800))
                self.screen.blit(picture, (0, 0))

                font = pygame.font.Font('game_font.ttf', 50)
                text = font.render(("Player " + winner + " Wins!" ), True, YELLOW)
                textRect = text.get_rect()
                textRect.center = (1200 // 2, 1500 // 2)
                self.screen.blit(text, textRect)

                font = pygame.font.Font('game_font.ttf', 50)
                text = font.render(("Press Space To Continue"), True, YELLOW)
                textRect = text.get_rect()
                textRect.center = (1200 // 2, 400 // 2)
                self.screen.blit(text, textRect)

                font = pygame.font.Font('game_font.ttf', 50)
                text = font.render(("Press Enter To Stop"), True, YELLOW)
                textRect = text.get_rect()
                textRect.center = (1200 // 2, 400)
                self.screen.blit(text, textRect)

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        exit()

                    elif event.key == pygame.K_SPACE:
                        return True

            pygame.display.update()

