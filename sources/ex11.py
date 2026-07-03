from matrix import Matrix 

def main():
    try:
        m1 = Matrix([[4, 1, 3, 7], [2, 5, 6, 8], [3, 6, 7, 9], [1, 2, 3, 4]])
        print(m1)
        print(m1.determinant())
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()