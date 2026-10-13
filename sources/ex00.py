from vector import Vector
from matrix import Matrix

def main():
    try:
        # Test valid operations
        print("=== Vector Operations ===")
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        print("v1:", v1)
        print("v2:", v2)
        print("v1 + v2:", v1.add(v2))
        print("v1 - v2:", v1.sub(v2))
        print("v1 * 2:", v1.scl(2))

        print("\n=== Matrix Operations ===")
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[5, 6], [7, 8]])
        print("M1:\n", m1, sep="")
        print("M2:\n", m2, sep="")
        print("M1 + M2:\n", m1.add(m2), sep="")
        print("M1 - M2:\n", m1.sub(m2), sep="")
        print("M1 * 3:\n", m1.scl(3), sep="")
        # Test edge cases
        print("\n=== Edge Cases ===")
        v3 = Vector([1, 2])
        try:
            print("v1 + v3 (different sizes):", v1.add(v3))
        except Exception as e:
            print(f"Error (expected): {e}")

        m3 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        try:
            print("m2 + m3 (different sizes):", m2.add(m3), sep="")
        except Exception as e:
            print(f"Error (expected): {e}")

        # Test invalid inputs
        try:
            Vector("not a list")
        except Exception as e:
            print(f"Error (expected): {e}")
        
        try:
            Matrix("not a list of lists")
        except Exception as e:
            print(f"Error (expected): {e}")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        




if __name__ == "__main__":
    main()
