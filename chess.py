from helper_functions import ChessBoardSetup, DrawBoard, MovePiece
from random_ai import GetRandomMove
import time
from minimax_ai import evl, GetMinMaxMove


def main():
    board = ChessBoardSetup()
    DrawBoard(board)
    print()
    MovePiece(board, (6, 0), (4, 0))
    DrawBoard(board)
    print()
    MovePiece(board, (1, 1), (3, 1))
    DrawBoard(board)
    print()
    MovePiece(board, (4, 0), (3, 1))
    DrawBoard(board)
    print(f"Value of board: {evl(board)}")


if __name__ == "__main__":
    main()
