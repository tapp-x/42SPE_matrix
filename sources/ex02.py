from vector import Vector
from matrix import Matrix


def lerp(a, b, t: float):
    """
    Computes the linear interpolation between two objects A and B
    using the parameter t, which should be in the range [0, 1].
    """
    if not isinstance(t, (int, float)):
        raise TypeError("Parameter t must be a scalar value (int or float).\n")
    if not (0 <= t <= 1):
        raise ValueError("Parameter t must be in the range [0, 1].\n")

    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a * (1 - t) + b * t
    if type(a) != type(b):
        raise TypeError("Input A and B must be of the same type.\n")
    if not isinstance(a, (Vector, Matrix)):
        raise TypeError("Input A must be a scalar, Vector or Matrix.\n")

    return a.scl(1 - t).add(b.scl(t))

def main():
    try:
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        t = 0.5
        print(f"Linear interpolation between 0 and 1 with t={t}: {lerp(0, 1, t)}")

        result_vector = lerp(v1, v2, t)
        print(f"Linear interpolation between {v1} and {v2} with t={t}: {result_vector}")

        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[5, 6], [7, 8]])
        result_matrix = lerp(m1, m2, t)
        print(f"Linear interpolation between\n{m1}\nand\n{m2}\nwith t={t}:\n{result_matrix}")

        print("\n When t=0, the result should be equal to A:")
        result_t0 = lerp(v1, v2, 0)
        print(f"Result with t=0: {result_t0}")

        print("\n When t=1, the result should be equal to B:")
        result_t1 = lerp(v1, v2, 1)
        print(f"Result with t=1: {result_t1}")

        print("\nTesting with invalid inputs:")
    except Exception as e:
        print(f"Error (expected): {e}")

    # Test with invalid inputs
    try:
        lerp("not an object vector/matrix", v2, t)
    except Exception as e:
        print(f"Error (expected): {e}")

    try:
        lerp(v1, m1, t)
    except Exception as e:
        print(f"Error (expected): {e}")

    try:
        lerp(v1, v2, 1.5)
    except Exception as e:
        print(f"Error (expected): {e}")
    
    try:
        lerp(v1, v2, -0.5)
    except Exception as e:
        print(f"Error (expected): {e}")

    try:
        v3 = Vector([1, 2])
        lerp(v1, v3, t)
    except Exception as e:
        print(f"Error (expected): {e}")

if __name__ == "__main__":
    main()