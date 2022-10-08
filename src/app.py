import pygame
from render import Render
from input import Input
from engine import Engine


class App:
    def __init__(self, screen_size):

        pygame.init()
        self.prev_selected_square = -1
        self.engine = Engine()
        self.render = Render(screen_size)
        self.input = Input()

    def run(self):
        while True:
            selected_square = self.input.detect_input(self.prev_selected_square)
            board, move, check = self.engine.play(selected_square)
            self.render.display_board(board, selected_square, move, check)
            self.prev_selected_square = selected_square
