from vector import Vector
from matrix import Matrix

from typing import TypeVar, Generic

K = TypeVar('K', int, float, complex)
V = TypeVar('V', Vector[K], Matrix[K])

def linear_interpolation(a: V, b: V, t: K) -> V:
    """
    Computes the linear interpolation between two objects A and B
    using the parameter t, which should be in the range [0, 1].
    """
    if not isinstance(a, (Vector, Matrix)):
        raise TypeError("Input A must be an instance of Vector or Matrix.\n")
    if not isinstance(b, (Vector, Matrix)):
        raise TypeError("Input B must be an instance of Vector or Matrix.\n")
    if type(a) != type(b):
        raise TypeError("Input A and B must be of the same type (both Vector or both Matrix).\n")
    if not isinstance(t, (int, float, complex)):
        raise TypeError("Parameter t must be a scalar value (int, float, or complex).\n")
    if not (0 <= t <= 1):
        raise ValueError("Parameter t must be in the range [0, 1].\n")

    return a.scl(1 - t).add(b.scl(t))

def main():
    try:
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        t = 0.5
        result_vector = linear_interpolation(v1, v2, t)
        print(f"Linear interpolation between {v1} and {v2} with t={t}: {result_vector}")

        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[5, 6], [7, 8]])
        result_matrix = linear_interpolation(m1, m2, t)
        print(f"Linear interpolation between\n{m1}\nand\n{m2}\nwith t={t}:\n{result_matrix}")

        print("\n When t=0, the result should be equal to A:")
        result_t0 = linear_interpolation(v1, v2, 0)
        print(f"Result with t=0: {result_t0}")

        print("\n When t=1, the result should be equal to B:")
        result_t1 = linear_interpolation(v1, v2, 1)
        print(f"Result with t=1: {result_t1}")

        print("\nTesting with invalid inputs:")
    except Exception as e:
        print(f"Error (expected): {e}")

    # Test with invalid inputs
    try:
        linear_interpolation("not an object vector/matrix", v2, t)
    except Exception as e:
        print(f"Error (expected): {e}")

    try:
        linear_interpolation(v1, m1, t)
    except Exception as e:
        print(f"Error (expected): {e}")

    try:
        linear_interpolation(v1, v2, 1.5)
    except Exception as e:
        print(f"Error (expected): {e}")
    
    try:
        linear_interpolation(v1, v2, -0.5)
    except Exception as e:
        print(f"Error (expected): {e}")

    try:
        v3 = Vector([1, 2])
        linear_interpolation(v1, v3, t)
    except Exception as e:
        print(f"Error (expected): {e}")

if __name__ == "__main__":
    main()