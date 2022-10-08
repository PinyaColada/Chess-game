import chess
import pygame


# Just a bunch of usefully functions
def get_legal_moves(board, selected_square):
    # We see which movements are legal from the selected square, this is not efficient but is not complex either
    moves = []
    square_name = chess.square_name(selected_square)
    for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
        for j in ['1', '2', '3', '4', '5', '6', '7', '8']:
            move = chess.Move.from_uci(square_name + i + j) if not square_name == (i + j) else None

            if move in board.legal_moves:
                moves.append(chess.parse_square(i + j))
            if is_the_move_going_to_promote(board, selected_square):
                move_with_prom = chess.Move.from_uci(square_name + i + j + 'q') if not square_name == (i + j) else None
                if move_with_prom in board.legal_moves:
                    moves.append(chess.parse_square(i + j))

    return chess.SquareSet(moves)


def is_the_move_going_to_promote(board, square):
    # Is the move going to promote?
    is_a_pawn = (board.piece_type_at(square) == chess.PAWN)
    is_white = (board.color_at(square) == chess.WHITE)
    if is_a_pawn and ((is_white and square_rank(square) == 6) or (not is_white and square_rank(square) == 1)):
        return True
    return False


def square_rank(square):
    # A little trick to compute the rank of a square
    # See the documentation of python-chess to know
    return square >> 3


def close_display():
    # Just close the display
    pygame.quit()
    quit()
