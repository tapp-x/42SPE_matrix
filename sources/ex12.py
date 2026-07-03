from matrix import Matrix

def main():
    try:
        m1 = Matrix([[1, 2], [3, 4]])
        print(" Try with matrix m1 :", m1)
        print("Inverse of m1 :")
        print(m1.inverse())

        print("And if we inverse the inverse :")
        m2 = m1.inverse()
        print(m2.inverse())
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()