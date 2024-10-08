from helper_functions import (
    get_piece,
    is_enemy,
    is_diagonal,
    is_same_column,
    is_same_row,
)


def IsClearPath(board: list[list[str]], from_square: tuple, to_square: tuple) -> bool:
    """Return True if the path between the two pieces is clear.

    Args:
        board (list[list[str]]): A 2-d array representing a chess board.
        from_square (tuple[int, int]): A tuple representing a position on the board.
        to_square (tuple[int, int]): A tuple representing a position on the board.

    Returns:
        bool: True if the path between the two squares is clear.
    """
    if from_square == to_square:
        return True
    else:
        row_diff = to_square[0] - from_square[0]
        col_diff = to_square[1] - from_square[1]

        if row_diff == 0:
            if col_diff > 0:
                new_from_square = (from_square[0], from_square[1] + 1)
            else:
                new_from_square = (from_square[0], from_square[1] - 1)
        elif col_diff == 0:
            if row_diff > 0:
                new_from_square = (from_square[0] + 1, from_square[1])
            else:
                new_from_square = (from_square[0] - 1, from_square[1])
        elif abs(row_diff) == abs(col_diff):
            if row_diff > 0 and col_diff > 0:
                new_from_square = (from_square[0] + 1, from_square[1] + 1)
            elif row_diff > 0 and col_diff < 0:
                new_from_square = (from_square[0] + 1, from_square[1] - 1)
            elif row_diff < 0 and col_diff > 0:
                new_from_square = (from_square[0] - 1, from_square[1] + 1)
            else:
                new_from_square = (from_square[0] - 1, from_square[1] - 1)
        else:
            return False

        if get_piece(board, new_from_square) != ".":
            return False
        else:
            return IsClearPath(board, new_from_square, to_square)


def IsMoveLegal(board: list[list[str]], from_square: tuple, to_square: tuple) -> bool:
    """Return True if the move is legal.

    Args:
        board (list[list[str]]): A 2-d array representing a chess board.
        from_square (tuple[int, int]): A tuple representing a position on the board.
        to_square (tuple[int, int]): A tuple representing a position on the board.

    Returns:
        bool: True if the move is legal.
    """
    if from_square == to_square:
        return False

    from_piece = get_piece(board, from_square)
    to_piece = get_piece(board, to_square)

    if from_piece == "p" or from_piece == "P":
        if (
            from_piece == "p"
            and to_piece == "."
            and to_square[1] == from_square[1]
            and to_square[0] - from_square[0] == 1
        ) or (
            from_piece == "P"
            and to_piece == "."
            and to_square[1] == from_square[1]
            and to_square[0] - from_square[0] == -1
        ):
            return True

        elif (
            from_piece == "p"
            and to_piece == "."
            and from_square[0] == 1
            and to_square[0] == 3
            and to_square[1] == from_square[1]
        ) or (
            from_piece == "P"
            and to_piece == "."
            and from_square[0] == 6
            and to_square[0] == 4
            and to_square[1] == from_square[1]
        ):
            if IsClearPath(board, from_square, to_square):
                return True
        elif (
            from_piece == "p"
            and to_piece != "."
            and to_square[0] - from_square[0] == 1
            and abs(to_square[1] - from_square[1]) == 1
            and is_enemy(from_piece, defending_piece=to_piece)
        ) or (
            from_piece == "P"
            and to_piece != "."
            and to_square[0] - from_square[0] == -1
            and abs(to_square[1] - from_square[1]) == 1
            and is_enemy(from_piece, defending_piece=to_piece)
        ):
            return True

    elif from_piece == "r" or from_piece == "R":
        if is_same_row(from_square, to_square) or is_same_column(
            from_square, to_square
        ):
            if is_enemy(from_piece, defending_piece=to_piece) or to_piece == ".":
                if IsClearPath(board, from_square, to_square):
                    return True

    elif from_piece == "b" or from_piece == "B":
        if is_diagonal(from_square, to_square):
            if is_enemy(from_piece, defending_piece=to_piece) or to_piece == ".":
                if IsClearPath(board, from_square, to_square):
                    return True

    elif from_piece == "q" or from_piece == "Q":
        if is_same_row(from_square, to_square) or is_same_column(
            from_square, to_square
        ):
            if is_enemy(from_piece, defending_piece=to_piece) or to_piece == ".":
                if IsClearPath(board, from_square, to_square):
                    return True

        if is_diagonal(from_square, to_square):
            if is_enemy(from_piece, defending_piece=to_piece) or to_piece == ".":
                if IsClearPath(board, from_square, to_square):
                    return True

    elif from_piece == "t" or from_piece == "T":
        col_diff = to_square[1] - from_square[1]
        row_diff = to_square[0] - from_square[0]

        if to_square == "." or is_enemy(from_piece, defending_piece=to_piece):
            if abs(col_diff) == 2 and abs(row_diff) == 1:
                return True
            elif abs(col_diff) == 1 and abs(row_diff) == 2:
                return True

    elif from_piece == "k" or from_piece == "K":
        col_diff = to_square[1] - from_square[1]
        row_diff = to_square[0] - from_square[0]

        if to_square == "." or is_enemy(from_piece, defending_piece=to_piece):
            if abs(col_diff) == 1 and abs(row_diff) == 1:
                return True
            elif abs(col_diff) == 1 and abs(row_diff) == 0:
                return True
            elif abs(col_diff) == 0 and abs(row_diff) == 1:
                return True

    return False


def GetListOfLegalMoves(
    board: list[list[str]], current_player: str, from_square: tuple
) -> list[tuple[int, int]]:
    """Return a list of legal moves for the piece at the given square.

    Args:
        board (list[list[str]]): A 2-d array representing a chess board.
        current_player (str): The current player.
        from_square (tuple[int, int]): A tuple representing a position on the board.

    Returns:
        list[tuple[int, int]]: A list of legal moves for the piece at the given square.
    """
    legal_moves = []
    for i in range(8):
        for j in range(8):
            if IsMoveLegal(board, from_square, (i, j)) and not DoesMovePutPlayerInCheck(
                board,
                from_square,
                (i, j),
                current_player,
            ):
                legal_moves.append((i, j))
    return legal_moves


def DoesMovePutPlayerInCheck(
    board: list[list[str]], from_square: tuple, to_square: tuple, current_player: str
) -> bool:
    """Return True if the move puts the player in check.

    Args:
        from_square (tuple[int, int]): A tuple representing a position on the board.
        to_square (tuple[int, int]): A tuple representing a position on the board.

    Returns:
        bool: True if the move puts the player in check.
    """
    from_piece = get_piece(board, from_square)

    board[from_square[0]][from_square[1]] = "."
    board[to_square[0]][to_square[1]] = from_piece

    is_in_check = IsInCheck(board, current_player)

    board[from_square[0]][from_square[1]] = from_piece
    board[to_square[0]][to_square[1]] = "."

    return is_in_check


def IsInCheck(board: list[list[str]], current_player: str) -> bool:
    """Return True if the player is in check.

    Args:
        board (list[list[str]]): A 2-d array representing a chess board.
        current_player (str): The current player.

    Returns:
        bool: True if the player is in check.
    """
    king_square = None
    for i in range(8):
        for j in range(8):
            if get_piece(board, (i, j)) == "k" and current_player == "b":
                king_square = (i, j)
            elif get_piece(board, (i, j)) == "K" and current_player == "w":
                king_square = (i, j)

    for i in range(8):
        for j in range(8):
            if get_piece(board, (i, j)) != "." and is_enemy(
                get_piece(board, (i, j)), defending_piece=get_piece(board, king_square)
            ):
                if IsMoveLegal(board, (i, j), king_square):
                    return True
    # for i in range(8):
    #     for j in range(8):
    #         if board[i][j] != ".":
    #             if (current_player == "white" and board[i][j].islower()) or (
    #                 current_player == "black" and board[i][j].isupper()
    #             ):
    #                 if IsMoveLegal(board, (i, j), king_square):
    #                     return True
    return False


def GetPiecesWithLegalMoves(board: list[list[str]], current_player: str) -> list[str]:
    """Return a list of pieces that have legal moves.

    Args:
        board (list[list[str]]): A 2-d array representing a chess board.
        current_player (str): The current player.

    Returns:
        list[str]: A list of pieces that have legal moves.
    """
    pieces_with_legal_moves = []
    for i in range(8):
        for j in range(8):
            piece = get_piece(board, (i, j))
            if piece != "." and not is_enemy(piece, current_player=current_player):
                if GetListOfLegalMoves(board, current_player, (i, j)):
                    pieces_with_legal_moves.append((i, j))
    return pieces_with_legal_moves


def IsCheckMate(board: list[list[str]], current_player: str):
    """Return True if the player is in checkmate.

    Args:
        board (list[list[str]]): A 2-d array representing a chess board.
        current_player (str): The current player.

    Returns:
        bool: True if the player is in checkmate.
    """
    if not GetPiecesWithLegalMoves(board, current_player):
        return True
    else:
        return False
