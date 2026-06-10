from vector import Vector
from typing import TypeVar

K = TypeVar('K', int, float, complex)


def linear_combination(u: list[Vector[K]], coefs: list[K]) -> Vector[K]:
    """
    Computes a linear combination of the vectors provided, 
    using the corresponding scalar coefficients.
    """
    if len(u) != len(coefs):
        raise ValueError("The number of vectors and coefficients must be the same.\n")
    
    for i in range(len(u)):
        if not isinstance(u[i], Vector):
            raise TypeError(f"Element {i} in the vector list is not a Vector instance.\n")
        if not isinstance(coefs[i], (int, float, complex)):
            raise TypeError(f"Element {i} in the coefficients list is not a valid scalar type.\n")

    print("Validating vector shapes...\n")
    print(f"All vectors must have the same shape. Expected shape: {u[0].shape()}\n")

    for i in range(1, len(u)):
        if u[i].shape() != u[0].shape():
            raise ValueError(f"All vectors must have the same shape. Vector {i} has shape {u[i].shape()}, expected {u[0].shape()}.\n")

    result = u[0].scl(coefs[0])
    for i in range(1, len(u)):
        result = result.add(u[i].scl(coefs[i]))
    return result

def main():
    try:
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        v3 = Vector([7, 8, 9])
        print(v1.shape())
        coefs = [0.5, 1.5, -1.0]
        result = linear_combination([v1, v2, v3], coefs)
        print("Description of the linear combination:\n")
        print(f"Linear combination of {v1}, {v2}, and {v3} with coefficients {coefs}")
        print("Expected result: 0.5 * v1 + 1.5 * v2 - 1.0 * v3")
        print("First operation: 0.5 * v1 =", v1.scl(0.5))
        print("Second operation: 1.5 * v2 =", v2.scl(1.5))
        print("Third operation: -1.0 * v3 =", v3.scl(-1.0))
        print("Adding the results together:")
        print(v1.scl(0.5), "+", v2.scl(1.5), "+", v3.scl(-1.0))
        print("Linear combination result:", result)
    except Exception as e:
        print(f"Error (expected): {e}")

if __name__ == "__main__":
    main()