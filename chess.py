from helper_functions import ChessBoardSetup, DrawBoard, MovePiece
from random_ai import GetRandomMove
import time
from min_max_ai import get_min_max_move


def main():
    board = ChessBoardSetup()

    while True:
        DrawBoard(board)
        time.sleep(3)
        print()
        print("White's turn")
        from_square, to_square = get_min_max_move(board, "w", 2)
        MovePiece(board, from_square, to_square)
        DrawBoard(board)
        time.sleep(3)
        print()
        print("Black's turn")
        from_square, to_square = get_min_max_move(board, "b", 2)
        MovePiece(board, from_square, to_square)


if __name__ == "__main__":
    main()
