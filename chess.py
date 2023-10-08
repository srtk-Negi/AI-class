from helper_functions import ChessBoardSetup, DrawBoard, get_piece
from random_ai import GetRandomMove
from chess_rules import IsMoveLegal, DoesMovePutPlayerInCheck


def main():
    board = ChessBoardSetup()
    DrawBoard(board)
    from_, to_ = GetRandomMove(board, "w")
    print(from_, to_)


if __name__ == "__main__":
    main()
