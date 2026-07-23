from vector import Vector
from matrix import Matrix

def main():
    m1 = Matrix([[1, 0], [0, 1]])
    v1 = Vector([4, 2])
    print("Matrix m1:\n", m1)
    print("Vector v1:", v1)
    print("Result of m1 * v1:", m1.mul_vec(v1))

    m2 = Matrix([[2, 0], [0, 2]])
    print("Matrix m2:\n", m2)
    print("Vector v1:", v1)
    print("Result of m2 * v1:", m2.mul_vec(v1))

    m3 = Matrix([[3, -5], [6, 8]])
    m4 = Matrix([[2, 1], [4, 2]])
    print("Matrix m3:\n", m3)
    print("Matrix m4:\n", m4)
    print("Result of m3 * m4:\n", m3.mul_mat(m4), sep="")

if __name__ == "__main__":
    main()