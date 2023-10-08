from helper_functions import ChessBoardSetup, DrawBoard
from random_ai import GetRandomMove
from chess_rules import IsMoveLegal, DoesMovePutPlayerInCheck


def main():
    board = ChessBoardSetup()
    DrawBoard(board)
    # print(IsMoveLegal(board, (6, 0), (4, 2)))
    # from_, to_ = GetRandomMove(board, "w")
    # print(from_, to_)
    GetRandomMove(board, "w")


if __name__ == "__main__":
    main()
