from helper_functions import (
    get_piece,
    is_enemy,
    is_diagonal,
    is_same_column,
    is_same_row,
)


def IsClearPath(board, from_square, to_square) -> bool:
    """Return True if the path between the two pieces is clear.

    Args:
        board (list[list[str]]): A 2-d array representing a chess board.
        from_square (tuple[int, int]): A tuple representing a position on the board.
        to_square (tuple[int, int]): A tuple representing a position on the board.

    Returns:
        bool: True if the path between the two pieces is clear.
    """
    from_x, from_y = from_square
    to_x, to_y = to_square

    if (from_x == to_x and abs(from_y - to_y) == 1) or (
        from_y == to_y and abs(from_x - to_x) == 1
    ):
        return True

    else:
        if to_x > from_x:
            new_from_square = (from_x + 1, from_y)
        elif to_x < from_x:
            new_from_square = (from_x - 1, from_y)
        elif to_y > from_y:
            new_from_square = (from_x, from_y + 1)
        elif to_y < from_y:
            new_from_square = (from_x, from_y - 1)
        elif to_x > from_x and to_y > from_y:
            new_from_square = (from_x + 1, from_y + 1)
        elif to_x > from_x and to_y < from_y:
            new_from_square = (from_x + 1, from_y - 1)
        elif to_x < from_x and to_y > from_y:
            new_from_square = (from_x - 1, from_y + 1)
        elif to_x < from_x and to_y < from_y:
            new_from_square = (from_x - 1, from_y - 1)

    if get_piece(board, new_from_square) != ".":
        return False
    else:
        return IsClearPath(board, new_from_square, to_square)


def IsMoveLegal(board, from_square, to_square) -> bool:
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
        ) or (
            from_piece == "P"
            and to_piece == "."
            and from_square[0] == 6
            and to_square[0] == 4
        ):
            if IsClearPath(board, from_square, to_square):
                return True
        elif (
            from_piece == "p"
            and to_piece != "."
            and to_square[0] - from_square[0] == 1
            and abs(to_square[1] - from_square[1]) == 1
            and is_enemy(from_piece, to_piece)
        ) or (
            from_piece == "P"
            and to_piece != "."
            and to_square[0] - from_square[0] == -1
            and abs(to_square[1] - from_square[1]) == 1
            and is_enemy(from_piece, to_piece)
        ):
            return True

    elif from_piece == "r" or from_piece == "R":
        if is_same_row(from_square, to_square) or is_same_column(
            from_square, to_square
        ):
            if is_enemy(from_piece, to_piece) or to_piece == ".":
                if IsClearPath(board, from_square, to_square):
                    return True

    elif from_piece == "b" or from_piece == "B":
        if is_diagonal(from_square, to_square):
            if is_enemy(from_piece, to_piece) or to_piece == ".":
                if IsClearPath(board, from_square, to_square):
                    return True

    elif from_piece == "q" or from_piece == "Q":
        if is_same_row(from_square, to_square) or is_same_column(
            from_square, to_square
        ):
            if is_enemy(from_piece, to_piece) or to_piece == ".":
                if IsClearPath(board, from_square, to_square):
                    return True

        if is_diagonal(from_square, to_square):
            if is_enemy(from_piece, to_piece) or to_piece == ".":
                if IsClearPath(board, from_square, to_square):
                    return True

    elif from_piece == "t" or from_piece == "T":
        col_diff = to_square[1] - from_square[1]
        row_diff = to_square[0] - from_square[0]

        if to_square == "." or is_enemy(from_piece, to_piece):
            if abs(col_diff) == 2 and abs(row_diff) == 1:
                return True
            elif abs(col_diff) == 1 and abs(row_diff) == 2:
                return True

    elif from_piece == "k" or from_piece == "K":
        col_diff = to_square[1] - from_square[1]
        row_diff = to_square[0] - from_square[0]

        if to_square == "." or is_enemy(from_piece, to_piece):
            if abs(col_diff) == 1 and abs(row_diff) == 1:
                return True
            elif abs(col_diff) == 1 and abs(row_diff) == 0:
                return True
            elif abs(col_diff) == 0 and abs(row_diff) == 1:
                return True
    else:
        return False


def GetListOfLegalMoves(board, current_player, from_square) -> list[tuple[int, int]]:
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


def DoesMovePutPlayerInCheck(board, from_square, to_square, current_player) -> bool:
    """Return True if the move puts the player in check.

    Args:
        from_square (tuple[int, int]): A tuple representing a position on the board.
        to_square (tuple[int, int]): A tuple representing a position on the board.

    Returns:
        bool: True if the move puts the player in check.
    """
    test_board = board.copy()

    from_piece = get_piece(test_board, from_square)

    test_board[from_square[0]][from_square[1]] = "."
    test_board[to_square[0]][to_square[1]] = from_piece

    return IsInCheck(test_board, current_player)


def IsInCheck(board, current_player) -> bool:
    """Return True if the player is in check.

    Args:
        board (list[list[str]]): A 2-d array representing a chess board.
        current_player (str): The current player.

    Returns:
        bool: True if the player is in check.
    """
