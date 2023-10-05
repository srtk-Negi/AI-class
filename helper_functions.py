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
    new_board = set_piece(set_piece(board, from_square, "."), to_square, piece_to_move)

    return new_board
