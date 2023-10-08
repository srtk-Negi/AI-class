def ChessBoardSetup() -> list[list[str]]:
    """Returns a 2-d array representing a chess board.
    The board is represented as a list of lists, where each inner list represents a row.
    Each element in the inner list represents a square on the board.

    The board is set up as follows:
    - The first row contains the black pieces.
    - The second row contains the black pawns.
    - The third and fourth rows are empty.
    - The fifth and sixth rows are empty.
    - The seventh row contains the white pawns.
    - The eighth row contains the white pieces.

    Returns:
        list[list[str]]: A 2-d array representing a chess board.
    """
    board = [
        ["r", "t", "b", "q", "k", "b", "t", "r"],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        ["R", "T", "B", "Q", "K", "B", "T", "R"],
    ]
    return board


def get_piece(board, position) -> str:
    """Returns the piece at the given position on the board.

    Args:
        board (list[list[str]]): A 2-d array representing a chess board.
        position (tuple[int, int]): A tuple representing a position on the board.

    Returns:
        str: The piece at the given position on the board.
    """
    x, y = position
    return board[x][y]


def set_piece(board, position, piece) -> list[list[str]]:
    """Sets the piece at the given position on the board.

    Args:
        board (list[list[str]]): A 2-d array representing a chess board.
        position (tuple[int, int]): A tuple representing a position on the board.
        piece (str): The piece to place on the board.

    Returns:
        list[list[str]]: A 2-d array representing a chess board.
    """
    x, y = position
    board[x][y] = piece
    return board


def DrawBoard(board) -> None:
    """Draws the board to the console.

    Args:
        board (list[list[str]]): A 2-d array representing a chess board.
    """
    for i in range(8):
        for j in range(8):
            print(f"{board[i][j]} ", end="")
        print()


def MovePiece(board, from_square, to_square) -> list[list[str]]:
    """Moves a piece from one square to another.

    Args:
        board (list[list[str]]): A 2-d array representing a chess board.
        from_square (tuple[int, int]): A tuple representing the square to move from.
        to_square (tuple[int, int]): A tuple representing the square to move to.

    Returns:
        list[list[str]]: A 2-d array representing a chess board.
    """
    piece_to_move = get_piece(board, from_square)
    new_board = set_piece(set_piece(board, from_square,
                          "."), to_square, piece_to_move)

    return new_board


def is_enemy(attacking_piece: str, **kwargs) -> bool:
    """Returns True if the defending piece is an enemy of the attacking piece.

    Args:
        attacking_piece (str): The piece that is attacking.
        **kwargs: Optional arguments.
            defending_piece (str): The piece that is defending.
            current_player (str): The current player.

    Returns:
        bool: True if the defending piece is an enemy of the attacking piece.
    """
    defending_piece = kwargs.get("defending_piece") if kwargs.get(
        "defending_piece") else None
    current_player = kwargs.get("current_player") if kwargs.get(
        "current_player") else None

    if defending_piece:
        if attacking_piece.isupper() and defending_piece.isupper():
            return False
        elif attacking_piece.islower() and defending_piece.islower():
            return False
        else:
            return True

    elif current_player:
        if attacking_piece.isupper() and current_player == "w":
            return False
        elif attacking_piece.islower() and current_player == "b":
            return False
        else:
            return True
    else:
        raise Exception(
            "Either defending_piece or current_player must be passed as a keyword argument.")


def is_diagonal(from_square, to_square) -> bool:
    """Returns True if the move is diagonal.

    Args:
        from_square (tuple[int, int]): A tuple representing a position on the board.
        to_square (tuple[int, int]): A tuple representing a position on the board.

    Returns:
        bool: True if the move is diagonal.
    """
    if abs(to_square[0] - from_square[0]) == abs(to_square[1] - from_square[1]):
        return True
    else:
        return False


def is_same_column(from_square, to_square) -> bool:
    """Returns True if the move is in the same column.

    Args:
        from_square (tuple[int, int]): A tuple representing a position on the board.
        to_square (tuple[int, int]): A tuple representing a position on the board.

    Returns:
        bool: True if the move is in the same column.
    """
    if to_square[1] == from_square[1]:
        return True
    else:
        return False


def is_same_row(from_square, to_square) -> bool:
    """Returns True if the move is in the same row.

    Args:
        from_square (tuple[int, int]): A tuple representing a position on the board.
        to_square (tuple[int, int]): A tuple representing a position on the board.

    Returns:
        bool: True if the move is in the same row.
    """
    if to_square[0] == from_square[0]:
        return True
    else:
        return False


def get_current_player(piece) -> str:
    """Returns the current player.

    Args:
        piece (str): The piece that is being moved.

    Returns:
        str: 'w' for white, 'b' for black.
    """
    if piece == ".":
        return None
    if piece.isupper():
        return "w"
    else:
        return "b"


def get_locations_of_all_pieces(board: list[list[str]], current_player: str) -> list[tuple[int, int]]:
    """Returns a list of the locations of all pieces belonging to the current player.

    Args:
        board (list[list[str]]): A 2-d array representing a chess board.
        current_player (str): 'w' for white, 'b' for black.

    Returns:
        list[tuple[int, int]]: A list of the locations of all pieces belonging to the current player.
    """
    locations = []
    for i in range(8):
        for j in range(8):
            if get_current_player(get_piece(board, (i, j))) == current_player:
                locations.append((i, j))
    return locations
