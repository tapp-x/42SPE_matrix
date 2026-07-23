from typing import Generic, TypeVar
from vector import Vector

K = TypeVar('K', int, float, complex)

class Matrix(Generic[K]):

    def __init__(self, data: list[list[K]]) -> None:
        if not isinstance(data, (list)):
            raise TypeError("Data must be a list of lists.")
        if len(data) == 0:
            raise ValueError("Data must have at least 1 row.")
        if not isinstance(data[0], (list)):
            raise TypeError("Data must be a list of lists.")
        row_length = len(data[0])
        if row_length == 0:
            raise ValueError("Matrix rows must have at least 1 element.")
        for row in data:
            if not isinstance(row, (list)):
                raise TypeError("Data must be a list of lists.")
            if len(row) != row_length:
                raise ValueError("All rows must have the same length.")
        self.data = [Vector(row) for row in data]

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
                    self.data[curr_line] = self.data[curr_line].scl(1 / pivot)

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

    def determinant(self) -> K:
        """ Computes the determinant of the matrix. """
        if not self.is_square():
            raise ValueError("Determinant is only defined for square matrices.")
            
        n = self.shape()[0]
        if n > 4:
            raise ValueError("Determinant calculation is only implemented for matrices up to 4x4.")
        
        if n == 2:
            return ((self.data[0].data[0] * self.data[1].data[1]) - (self.data[0].data[1] * self.data[1].data[0]))

        det = 0
        for col in range(n):
            
            scalar = self.data[0].data[col]
            
            sign = (-1) ** col

            sub_matrix = []

            for row in range(1, n):
                sub_row = []
                for x in range(n):
                    if x == col:
                        continue
                    sub_row.append(self.data[row].data[x])
                sub_matrix.append(sub_row)
            det += sign * scalar * Matrix(sub_matrix).determinant()
        
        return det

    def inverse(self) -> 'Matrix[K]':
        """ Computes and return the inverse of a Matrix, if not possible, raise an error"""
        if not self.is_square():
            raise ValueError("Inverse is only possible for square matrices.")

        det = self.determinant
        if det == 0:
            raise ValueError("The Matrix given is singular (det = 0), cannot compute the inverse")

        line_len, col_len = self.shape()

        augmented_matrix = []
        for col, row in enumerate(self.data):

            initial_matrix = list(row.data)

            identitiy_matrix = [1.0 if j == col else 0.0 for j in range(line_len)]
            augmented_matrix.append(Vector(initial_matrix + identitiy_matrix))

        curr_line = 0
        for curr_col in range(col_len):
            pivot_found = False
            
            for search_line in range(curr_line, line_len):
                pivot = augmented_matrix[search_line].data[curr_col]
                
                if pivot != 0: 
                    # SWAP
                    if search_line > curr_line:
                        augmented_matrix[curr_line], augmented_matrix[search_line] = augmented_matrix[search_line], augmented_matrix[curr_line]
                    
                    # NORMALISATION
                    actual_pivot = augmented_matrix[curr_line].data[curr_col]
                    augmented_matrix[curr_line] = augmented_matrix[curr_line].scl(1 / actual_pivot)
                    
                    pivot_found = True
                    break
                    
            if not pivot_found:
                raise ValueError("Matrix is singular and cannot be inverted (determinant is 0).")
                
            # CLEAN
            for target_line in range(line_len):
                if target_line != curr_line:
                    factor = augmented_matrix[target_line].data[curr_col]
                    augmented_matrix[target_line] = augmented_matrix[target_line].sub(augmented_matrix[curr_line].scl(factor))
                    
            curr_line += 1
            if curr_line >= line_len:
                break
                
        inverse_data = []
        for row in augmented_matrix:
            inverse_data.append(row.data[col_len:])
            
        return Matrix(inverse_data)

    def rank(self) -> int:
        """ Computes and returns the rank of the matrix. """
        row_echelon_matrix = self.row_echelon()
        rank = 0
        for row in row_echelon_matrix.data:
            if any(value != 0 for value in row.data):
                rank += 1
        return rank