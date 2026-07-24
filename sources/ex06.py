from vector import Vector

def cross_product(v1: Vector, v2: Vector) -> Vector:
    if v1.shape() != 3 or v2.shape() != 3:
        raise ValueError("Cross product is only defined for 3-dimensional vectors.")
    
    a1, a2, a3 = v1.data
    b1, b2, b3 = v2.data
    
    cross_prod = [
        a2 * b3 - a3 * b2,
        a3 * b1 - a1 * b3,
        a1 * b2 - a2 * b1
    ]
    
    return Vector(cross_prod)


def main():
    try:
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])

        print("v1:", v1)
        print("v2:", v2)
        print("Cross product of v1 and v2:", cross_product(v1, v2))


        v4 = Vector([4, 2, -3])
        v5 = Vector([-2, -5, 16])
        print("v4:", v4)
        print("v5:", v5)
        print("Cross product of v4 and v5:", cross_product(v4, v5))

    except ValueError as e:
        print("Error:", e)

    # Test with invalid inputs 
    try:
        v3 = Vector([1, 2])
        cross_prod = cross_product(v1, v3)
    except ValueError as e:
        print("Error:", e)

    try:
        v4 = Vector([0, 0, 0])
        cross_prod = cross_product(v1, v4)
        print("Cross product of v1 and v4:", cross_prod)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()