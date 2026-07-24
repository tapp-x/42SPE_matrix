from vector import Vector

def main():
    try:
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        print("v1:", v1)
        print("Norm 1 of v1:", v1.norm_1())
        print("Norm 2 of v1:", v1.norm())
        print("Norm inf of v1:", v1.norm_inf())

        print("v2:", v2)
        print("Norm 1 of v2:", v2.norm_1())
        print("Norm 2 of v2:", v2.norm())
        print("Norm inf of v2:", v2.norm_inf())
    
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()