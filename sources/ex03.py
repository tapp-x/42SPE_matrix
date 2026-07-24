from vector import Vector

def main():
    try:
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        print("v1:", v1)
        print("v2:", v2)
        print("Dot product:", v1.dot(v2))
    except Exception as e:
        print("Error:", e)

    try:
        v3 = Vector([1, 2])
        print("v3:", v3)
        print("Dot product:", v1.dot(v3))
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()