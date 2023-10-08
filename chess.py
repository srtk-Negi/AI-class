from helper_functions import ChessBoardSetup, DrawBoard, MovePiece
from random_ai import GetRandomMove
import time
from minimax_ai import evl, GetMinMaxMove


def main():
    board = ChessBoardSetup()
    DrawBoard(board)
    print(f"Board Value - {evl(board)}")
    from_, to_ = GetRandomMove(board, "w")
    MovePiece(board, from_, to_)
    print(f"Board Value - {evl(board)}")
    from_, to_ = GetRandomMove(board, "b")
    MovePiece(board, from_, to_)
    print(f"Board Value - {evl(board)}")


if __name__ == "__main__":
    main()
