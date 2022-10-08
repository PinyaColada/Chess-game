import chess
import pygame
from utils import close_display


class Input:
    def __init__(self):
        self.CLOSE_WINDOW_KEY = pygame.K_ESCAPE
        self.TEST_KEY = pygame.K_3

        # These constants are hard coded for a size of 700
        self.FRAMEWORK_MAXIMUM_VALUE = 673
        self.FRAMEWORK_MINIMUM_VALUE = 27
        self.SQUARE_SIZE = 82

    def detect_input(self, selected_square):
        keys = pygame.key.get_pressed()
        events = pygame.event.get()

        for ev in events:
            if ev.type == pygame.QUIT or keys[self.CLOSE_WINDOW_KEY]:
                close_display()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                square = self.select_square()
                if not square == 'Outside':
                    return chess.parse_square(square)
                return -1

        return selected_square

    def select_square(self):
        # This way we can know where the player clicked
        x_cords = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        y_cords = ['8', '7', '6', '5', '4', '3', '2', '1']
        pos_x, pos_y = pygame.mouse.get_pos()

        if (pos_x <= self.FRAMEWORK_MINIMUM_VALUE) or (pos_x >= self.FRAMEWORK_MAXIMUM_VALUE) or \
           (pos_y <= self.FRAMEWORK_MINIMUM_VALUE) or (pos_y >= self.FRAMEWORK_MAXIMUM_VALUE):
            return 'Outside'
        else:
            aux_1 = x_cords[(pos_x - self.FRAMEWORK_MINIMUM_VALUE) // self.SQUARE_SIZE]
            aux_2 = y_cords[(pos_y - self.FRAMEWORK_MINIMUM_VALUE) // self.SQUARE_SIZE]
            return aux_1 + aux_2

