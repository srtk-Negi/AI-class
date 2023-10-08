import random
from chess_rules import GetListOfLegalMoves, GetPiecesWithLegalMoves
from helper_functions import get_locations_of_all_pieces


def GetRandomMove(board: list[list[str]], current_player):
    """Returns a random move for the current player"""
    pieces_with_legal_moves = GetPiecesWithLegalMoves(board, current_player)
    print(pieces_with_legal_moves)
    # random_from_square = random.choice(pieces_with_legal_moves)

    # legal_moves = GetListOfLegalMoves(board, current_player, (7, 1))
    # print(legal_moves)

    # print(random_piece_to_move_loc, random_legal_move)
    # return (random_piece_to_move_loc, random.choice(GetListOfLegalMoves(board, current_player, random_piece_to_move_loc)))
