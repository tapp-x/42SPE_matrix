from matrix import Matrix

def main():
    m1 = Matrix(
        [[1, 0, 0],
         [0, 1, 0],
         [0, 0, 1]]
    )
    print("Matrix m1:\n", m1)
    print("Trace of m1:", m1.trace())

    m2 = Matrix(
        [[2, -5, 0],
         [4, 3, 7],
         [-2, 3, 4]]
    )
    print("Matrix m2:\n", m2)
    print("Trace of m2:", m2.trace())

    m3 = Matrix(
        [[-2, -8, 4],
         [1, -23, 4],
         [0, 6, 4]]
    )
    print("Matrix m3:\n", m3)
    print("Trace of m3:", m3.trace())

    try:
        m4 = Matrix(
            [[1, 2, 3],
             [4, 5]]
        )
        print("Matrix m4:\n", m4)
        print("Trace of m4:", m4.trace())
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()  