""" Min-Max AI for Chess."""
from chess_rules import GetPiecesWithLegalMoves, GetListOfLegalMoves
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


def GetMinMaxMove(board: list[list[str]], current_player: str) -> tuple[tuple[int, int], tuple[int, int]]:
    """Returns the best move for the current player.

    Args:
        board (list[list[str]]): A 2-d array representing a chess board.
        current_player (str): 'w' for white, 'b' for black.

    Returns:
        tuple[tuple[int, int], tuple[int, int]]: A tuple representing the best move for the current player.
    """
    best_move = 0
    best_enemy_move = 0

    best_score = 0
    best_enemy_score = 0

    enemy_player = "b" if current_player == "w" else "w"

    pieces = GetPiecesWithLegalMoves(board, current_player)

    for piece in pieces:
        legal_moves = GetListOfLegalMoves(board, current_player, piece)
        for move in legal_moves:
            MovePiece(board, piece, move)
            enemy_pieces = GetPiecesWithLegalMoves(board, enemy_player)
            for enemy_piece in enemy_pieces:
                enemy_legal_moves = GetListOfLegalMoves(
                    board, enemy_player, enemy_piece)
                for enemy_move in enemy_legal_moves:
                    MovePiece(board, enemy_piece, enemy_move)
                    res = evl(board)
                    best_enemy_move = enemy_move if res < best_enemy_score else best_enemy_move
                    MovePiece(board, enemy_move, enemy_piece)

            MovePiece(board, move, piece)
