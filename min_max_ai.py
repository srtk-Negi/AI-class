""" Min-Max AI for Chess."""
from chess_rules import GetPiecesWithLegalMoves
from helper_functions import MovePiece


def evl(board: list[list[str]], current_player: str, depth: int) -> int:
    """ Evaluation function. """
    if depth == 0:
        return 0
    pieces = GetPiecesWithLegalMoves(board, current_player)
    score = 0
    for piece in pieces:
        score += len(pieces[piece])
    return score


def get_min_max_move(board: list[list[str]], current_player: str, depth: int) -> tuple[tuple[int, int], tuple[int, int]]:
    """ Min-Max algorithm. """
    pieces = GetPiecesWithLegalMoves(board, current_player)
    best_move = None
    best_score = None
    for piece in pieces:
        for move in pieces[piece]:
            MovePiece(board, piece, move)
            score = evl(board, current_player, depth - 1)
            MovePiece(board, move, piece)
            if best_score is None or score > best_score:
                best_score = score
                best_move = (piece, move)
    return best_move
