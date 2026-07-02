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


    def mul_vec(self, vector: Vector[K]) -> Vector[K]:
        """ Multiplies a matrix by a vector. """
        if self.shape()[1] != vector.shape():
            raise ValueError("Matrix columns must match vector size for multiplication.")
        result_data = [row.dot(vector) for row in self.data]
        return Vector(result_data)
    
    def mul_mat(self, other: 'Matrix[K]') -> 'Matrix[K]':
        """ Multiplies two matrices together. """
        if self.shape()[1] != other.shape()[0]:
            raise ValueError("Matrix A's columns must match Matrix B's rows for multiplication.")
        result_data = []
        for row in self.data:
            new_row = [row.dot(Vector(col)) for col in zip(*other.data)]
            result_data.append(new_row)
        return Matrix(result_data)

    def trace(self) -> K:
        """ Returns the trace of the matrix (sum of diagonal elements). """
        if not self.is_square():
            raise ValueError("Trace is only defined for square matrices.")
        return sum(self.data[i].data[i] for i in range(self.shape()[0]))

    def transpose(self) -> 'Matrix[K]':
        """ Returns the transpose of the matrix. """
        transposed_data = [[self.data[j].data[i] for j in range(self.shape()[0])] for i in range(self.shape()[1])]
        return Matrix(transposed_data)

    def row_echelon(self) -> 'Matrix[K]':
        """ Computes and returns the row echelon form of the Matrix"""
        curr_line = 0
        line_len, col_len = self.shape()

        for curr_col in range(col_len):
            pivot_found = False

            for search_line in range(curr_line, line_len):
                pivot = self.data[search_line].data[curr_col] 
                if (pivot != 0):
                    # SWAP
                    if (search_line > curr_line):
                        self.data[curr_line], self.data[search_line] = self.data[search_line], self.data[curr_line]

                    # NORMALIZATION
                    self.data[search_line] = self.data[search_line].scl(1 / pivot)

                    pivot_found = True
                    break

            if pivot_found:
                for target_line in range(line_len):
                    if (target_line != curr_line):
                    # SET 0 IN PIVOT COLUMN
                        self.data[target_line] = self.data[target_line].sub(self.data[curr_line].scl(self.data[target_line].data[curr_col]))

                curr_line += 1

                if curr_line >= line_len:
                    break

        return self

