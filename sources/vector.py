from typing import Generic, TypeVar

K = TypeVar('K', int, float, complex)

class Vector(Generic[K]):
    """ A simple vector class that can hold vectors of any dimension. """

    def __init__(self, data: list[K]) -> None:
        if not isinstance(data, (list)):
            raise TypeError("Data must be a list.")
        if len(data) < 2:
            raise ValueError("Data must have at least 2 elements.")
        self.data = data

    def __str__(self) -> str:
        return f"Vector({', '.join(str(x) for x in self.data)})"

    def shape(self) -> int:
        """ Returns the dimension of the vector. """
        return len(self.data)

    def add(self, other: 'Vector[K]') -> 'Vector[K]':
        """ Adds two vectors together. """
        if self.shape() != other.shape():
            raise ValueError("Vectors must have the same shape to be added.")
        return Vector([a + b for a, b in zip(self.data, other.data)])

    def sub(self, other: 'Vector[K]') -> 'Vector[K]':
        """ Subtracts one vector from another. """
        if self.shape() != other.shape():
            raise ValueError("Vectors must have the same shape to be subtracted.")
        return Vector([a - b for a, b in zip(self.data, other.data)])

    def scl(self, scalar: K) -> 'Vector[K]':
        """ Multiplies a vector by a scalar. """
        return Vector([scalar * x for x in self.data])
    
    def ecl(self, other: 'Vector[K]') -> float:
        """ Computes the Euclidean distance between two vectors. """
        if self.shape() != other.shape():
            raise ValueError("Vectors must have the same shape to compute distance.")
        return sum((a - b) ** 2 for a, b in zip(self.data, other.data)) ** 0.5

    def dot(self, other: 'Vector[K]') -> K:
        """ Computes the dot product of two vectors. """
        if self.shape() != other.shape():
            raise ValueError("Vectors must have the same shape to compute dot product.")
        return sum(a * b for a, b in zip(self.data, other.data))

    def norm_1(self) -> float:
        """ Computes the norm 1 of the vector. Also known as the Manhattan norm.
        That's the sum of the absolute values of the vector's components. """
        return float(sum(abs(x) for x in self.data))

    def norm(self) -> float:
        """ Computes the norm 2 of the vector. Also known as the Euclidean norm.
        That's the square root of the sum of the squares of the vector's components. """
        square_sum = sum(x ** 2 for x in self.data)
        return square_sum ** 0.5

    def norm_inf(self) -> float:
        """ Computes the norm inf of the vector. Also known as the Chebyshev norm.
        That's the maximum absolute value among the vector's components. """
        return float(max(abs(x) for x in self.data))