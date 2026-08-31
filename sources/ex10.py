from matrix import Matrix 

def main():
    m1 = Matrix([[4, 1], [2, 6]])
    print("Original matrix : ", m1)
    m1 = m1.row_echelon()

    print("After row echelon : ", m1)

    m2 = Matrix([
        [8, 5, -2, 4, 28],
        [4, 2.5, 20, 4, -4],
        [8, 5, 1, 4, 17],
    ])
    print("Original matrix : \n", m2)
    m2 = m2.row_echelon()
    print("After row echelon : \n", m2)

if __name__ == "__main__":
    main()