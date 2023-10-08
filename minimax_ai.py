""" Min-Max AI for Chess."""
from chess_rules import GetPiecesWithLegalMoves
from helper_functions import MovePiece, get_piece


def evl(board):
    piece_value = {
        "p": 1,
        "t": 3,
        "b": 3,
        "r": 5,
        "q": 9,
        "k": 10
    }
    white_value = 0
    black_value = 0

    for i in range(8):
        for j in range(8):
            piece = get_piece(board, (i, j))
            if piece != ".":
                if piece.isupper():
                    white_value += piece_value[piece.lower()]
                else:
                    black_value += piece_value[piece]

    return white_value - black_value


def GetMinMaxMove():
    pass
