from matrix import Matrix 

def main():
    try:
        m1 = Matrix([[1, 2, 3], [4, 5, 6]])
        print("Original matrix:")
        print(m1)
        
        m1_transposed = m1.transpose()
        print("\nTransposed matrix:")
        print(m1_transposed)
        
        m3 = Matrix([[1], [2], [3]])
        print("\nOriginal matrix (single column):")
        print(m3)
        print("Transposed:")
        print(m3.transpose())

        m4 = Matrix([[1], [2, 3]])
        print("\nOriginal matrix (mixed dimensions):")
        print(m4)
        print("Transposed:")
        print(m4.transpose())

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()