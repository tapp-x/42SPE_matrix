from typing import Generic, TypeVar
from vector import Vector

K = TypeVar('K', int, float, complex)

class Matrix(Generic[K]):

    def __init__(self, data: list[list[K]]) -> None:
        if not isinstance(data, (list)):
            raise TypeError("Data must be a list of lists.")
        if len(data) < 2:
            raise ValueError("Data must have at least 2 rows.")
        row_length = len(data[0])
        for row in data:
            if not isinstance(row, (list)):
                raise TypeError("Data must be a list of lists.")
            if len(row) != row_length:
                raise ValueError("All rows must have the same length.")
        self.data = data
        for i in range(len(data)):
            self.data[i] = Vector(data[i])

    def __str__(self) -> str:
        """ Returns a string representation of the matrix. """
        return "\n".join(f"[{', '.join(str(x) for x in row.data)}]" for row in self.data)

    def shape(self) -> tuple[int, int]:
        """ Returns the shape of the matrix as (rows, columns). """
        return (len(self.data), len(self.data[0].data))

    def is_square(self) -> bool:
        """ Checks if the matrix is square. """
        return self.shape()[0] == self.shape()[1]

    def add(self, other: 'Matrix[K]') -> 'Matrix[K]':
        """ Adds two matrices together. """
        if self.shape() != other.shape():
            raise ValueError("Matrices must have the same shape to be added.")
        return Matrix([row.add(other.data[i]).data for i, row in enumerate(self.data)])

    def sub(self, other: 'Matrix[K]') -> 'Matrix[K]':
        """ Subtracts one matrix from another. """
        if self.shape() != other.shape():
            raise ValueError("Matrices must have the same shape to be subtracted.")
        return Matrix([row.sub(other.data[i]).data for i, row in enumerate(self.data)])

    def scl(self, scalar: K) -> 'Matrix[K]':
        """ Multiplies a matrix by a scalar. """
        return Matrix([row.scl(scalar).data for row in self.data])