from helper_functions import is_diagonal


def main():
    print(is_diagonal((1, 2), (2, 1)))
    print(is_diagonal((1, 2), (3, 0)))
    print(is_diagonal((1, 2), (4, 1)))
    print(is_diagonal((1, 2), (1, 1)))
    print(is_diagonal((4, 7), (6, 5)))


if __name__ == "__main__":
    main()
