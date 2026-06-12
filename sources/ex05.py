from vector import Vector 
from typing import TypeVar

K = TypeVar('K', int, float, complex)

def angle_cos(v1: Vector[K], v2: Vector[K]) -> float:
    if v1.shape() != v2.shape():
        raise ValueError("Vectors must have the same shape to compute angle.")
    dot_product = v1.dot(v2)
    norm_v1 = v1.norm()
    norm_v2 = v2.norm()
    if norm_v1 == 0 or norm_v2 == 0:
        raise ValueError("Cannot compute angle with zero vector.")
    return dot_product / (norm_v1 * norm_v2)

if __name__ == "__main__":
    try:
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])

        print("v1:", v1)
        print("v2:", v2)
        print("Angle cosine between v1 and v2:", angle_cos(v1, v2))

    except ValueError as e:
        print("Error:", e)

    # Test with invalid inputs 
    try:
        v3 = Vector([1])
        angle = angle_cos(v1, v3)
    except ValueError as e:
        print("Error:", e)

    try:
        v4 = Vector([0, 0, 0])
        angle = angle_cos(v1, v4)
    except ValueError as e:
        print("Error:", e)