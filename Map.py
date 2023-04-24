import csv
import pygame

#Constants declaration
GREEN = (20, 255, 140)
GREY = (210, 210, 210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

#The map loads the positions of the map, draws the map and detects collisions with the map
#TODO: Within the init method, load the file into an array of y values
#TODO: Change draw method to draw from the array of y values
#TODO: Add is_collision method to compare to array of y values.
class Map():
    screen = None  #Pygame object used to draw with
    map_y = []
    map_selection = None

    def __init__(self, screen, map_selection):
        self.screen = screen
        with open("map" + str(map_selection) + ".csv", 'r') as file:
            #Seperates the regions between the intergers using commas
            reader = csv.reader(file)
            for row in reader:

                count = 0
                for pos_y in row:
                    self.map_y.append(pos_y)

    def draw(self):

        for count in range(len(self.map_y)):
            pos_y = self.map_y[count]
            end_pos = (count, int(pos_y))
            start_pos = (count, 800)
            # Draws a line from the start_pos, the bottom of the screen, to the end_pos, the coordinates found
            # using the map_y_coordinate. The final number in the brackets is the line width.
            pygame.draw.line(self.screen, GREEN, start_pos, end_pos, 1)

    def is_collision(self, pos_x, pos_y):

        # This prevents the projectile from going past either side of the screen
        if pos_x >= len(self.map_y) or pos_x <= 0:
            return True

        # This find out if the projectile has collided with the map, using the array of map y coordinates
        if int(self.map_y[int(pos_x)]) < int(pos_y):
            return True
        else:

            return False

