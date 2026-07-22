from matrix import Matrix


def main():
    try:
        m1 = Matrix([
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0],
        ])
        print(m1.rank())

        m2 = Matrix([
            [1.0, 2.0, 0.0, 0.0],
            [2.0, 4.0, 0.0, 0.0],
            [-1.0, 2.0, 1.0, 1.0],
        ])
        print(m2.rank())

        m3 = Matrix([
            [8.0, 5.0, -2.0],
            [4.0, 7.0, 20.0],
            [7.0, 6.0, 1.0],
            [21.0, 18.0, 7.0],
        ])
        print(m3.rank())

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
    