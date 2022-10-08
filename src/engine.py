import chess
from utils import get_legal_moves, is_the_move_going_to_promote, close_display


class Engine:
    def __init__(self):
        self.prev_selected_square = -1
        self.selected_square = -1
        self.move = chess.Move(-1, -1)
        self.board = chess.Board()
        self.color = True
        self.check = None

    def play(self, selected_square):
        if not self.selected_square == selected_square:
            # If there is two selection and the movement is legal then we apply the move
            self.prev_selected_square, self.selected_square = self.selected_square, selected_square
            if not self.prev_selected_square == -1:
                # This is only if we selected an square and not clicked outside the board
                if selected_square in get_legal_moves(self.board, self.prev_selected_square):  # Is the movement legal?
                    # If is a pawn in the last line then we know is going to be a promotion
                    if is_the_move_going_to_promote(self.board, self.prev_selected_square):
                        move = chess.Move(self.prev_selected_square, self.selected_square, promotion=chess.QUEEN)
                    else:
                        move = chess.Move(self.prev_selected_square, self.selected_square)
                    self.board.push(move)  # We apply the move
                    self.move = move  # We record the move
                    self.color = not self.color  # Then is the turn for the other color

                    # We apply a lot of checks to know if it is a win or a draw
                    if self.board.is_check():
                        self.check = self.board.king(self.color)
                    else:
                        self.check = None

                    if self.board.is_checkmate():
                        print("Checkmate")
                        if self.color:
                            print('Black player wins')
                        else:
                            print('White player wins')
                        close_display()

                    if self.board.has_insufficient_material(True):
                        print('White does not have sufficient material, black wins')

                    if self.board.has_insufficient_material(True):
                        print('Black does not have sufficient material, black wins')

                    if self.board.is_stalemate() or self.board.is_repetition() or self.board.is_fifty_moves():
                        print('Draw')
                        close_display()

                    return self.board, self.move, self.check

        return self.board, self.move, self.check
