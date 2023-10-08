import random
from chess_rules import GetListOfLegalMoves, GetPiecesWithLegalMoves


def GetRandomMove(board: list[list[str]], current_player) -> tuple[tuple[int, int], tuple[int, int]]:
    """Returns a random move for the current player"""
    pieces_with_legal_moves = GetPiecesWithLegalMoves(board, current_player)
    random_from_square = random.choice(pieces_with_legal_moves)

    legal_moves = GetListOfLegalMoves(
        board, current_player, random_from_square)
    random_to_square = random.choice(legal_moves)

    return random_from_square, random_to_square
