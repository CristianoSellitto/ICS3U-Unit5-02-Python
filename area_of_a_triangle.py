#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in November 2022
# A program that calculates the area of a triangle


def calculate_triangle_area(base, height):
    # Calculates the area of a triangle

    area = (base * height) / 2
    # Checks if the area is a whole number so there is no ".0" at the end
    if area % 1 == 0:
        area = int(area)
    print("\nThe area of this triangle is {} cm²".format(area))


def main():
    # Gets input from the user

    try:
        print("A = (b × h) ÷ 2")
        base_text = input("\nEnter a base integer: ")
        base_integer = int(base_text)
        height_text = input("Enter a height integer: ")
        height_integer = int(height_text)
        calculate_triangle_area(base_integer, height_integer)
    except ValueError:
        print("\nError: {} isn't an integer.".format(base_text))
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
