from helper_functions import ChessBoardSetup, DrawBoard, MovePiece
from minimax_ai import GetMinMaxMove
from random_ai import GetRandomMove
from chess_rules import IsCheckMate
import time


def main():
    board = ChessBoardSetup()
    player_1 = "w"
    player_2 = "b"
    current = player_1
    turns = 0
    N = 100
    while not IsCheckMate(board, current) and turns < N:
        DrawBoard(board)
        if current == player_1:
            move = GetMinMaxMove(board, current)
            print("\nWHITE / MinMaxAI plays!\n")
        else:
            turns += 1
            move = GetRandomMove(board, current)
            print("\nBLACK / RandomAI plays!\n")
        MovePiece(board, move[0], move[1])
        current = player_1 if current == player_2 else player_2
        DrawBoard(board)
        print()
        time.sleep(0.5)

    if IsCheckMate(board, current):
        print(f"\n{current} is checkmate!")
    else:
        print(f"\nDraw after {N} turns!")


if __name__ == "__main__":
    main()
