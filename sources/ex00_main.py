from vector import Vector
from matrix import Matrix

import time

def test_complexity(size: int) -> None:
    """ Tests the time complexity of vector and matrix operations. """
    v1 = Vector(list(range(size)))
    v2 = Vector(list(range(size)))
    m1 = Matrix([list(range(size)) for _ in range(size)])
    m2 = Matrix([list(range(size)) for _ in range(size)])

    start_time = time.time()
    v1.add(v2)
    print(f"Vector addition of size {size} took {time.time() - start_time:.6f} seconds.")

    start_time = time.time()
    m1.add(m2)
    print(f"Matrix addition of size {size}x{size} took {time.time() - start_time:.6f} seconds.")

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
        # Test complexity time operations

        print("\n=== Complexity Tests ===")
        test_complexity(100)
        test_complexity(200)
        test_complexity(400)

        # Test edge cases
        print("\n=== Edge Cases ===")
        v3 = Vector([1, 2])
        try:
            print("v1 + v3 (different sizes):", v1.add(v3))
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