import pygame
import chess
from chess import svg
import cairosvg
from PIL import Image
import io
from utils import get_legal_moves


class Render:
    def __init__(self, size):
        self.size = size

        self.NAME = 'μ-Chess'
        self.LOGO_FILEPATH = 'Images/Logo.png'
        self.FRAME_FILEPATH = 'Images/frame.png'
        self.last_board = None
        self.last_selection = -1

        # flags = pygame.RESIZABLE
        logo = pygame.image.load(self.LOGO_FILEPATH)
        self.display_surf = pygame.display.set_mode((size, size), 0, 32)

        pygame.display.set_caption(self.NAME)
        pygame.display.set_icon(logo)

    def display_board(self, board, selected_square, move, check):
        # We dont need to apply a change in the frame that pygame shows if the player has not made and clicks
        if board != self.last_board or selected_square != self.last_selection:
            self.last_board = board
            self.last_selection = selected_square
            # We apply a lot a of conditionals to know which parameters to pass to svg.board()
            if not selected_square == -1:
                if (self.last_selection != -1) and (selected_square in get_legal_moves(board, self.last_selection)):
                    board_svg = chess.svg.board(board, size=self.size, lastmove=move, check=check)
                else:
                    movements = get_legal_moves(board, selected_square)
                    if len(movements) > 0:
                        sel_fill = dict.fromkeys(movements, "#96a5ff77") | {selected_square: "#96ff9688"}
                        board_svg = chess.svg.board(board, size=self.size, fill=sel_fill, lastmove=move, check=check)
                    else:
                        board_svg = chess.svg.board(board, size=self.size, lastmove=move, check=check)
            else:
                board_svg = chess.svg.board(board, size=self.size, lastmove=move, check=check)  # We get the svg

            aux = cairosvg.svg2png(board_svg, output_width=self.size, output_height=self.size)  # We convert it to png
            image = Image.open(io.BytesIO(aux))  # Then we convert to a PIL.image
            raw_str = image.tobytes("raw", 'RGBA')  # Finally we get the raw data from the PIL image
            board_surf = pygame.image.frombuffer(raw_str, (self.size, self.size), 'RGBA')  # And then we display it

            self.display_surf.fill((0, 0, 0))
            self.display_surf.blit(board_surf, (0, 0))

            pygame.display.update()
