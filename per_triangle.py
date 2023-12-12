#!/usr/bin/env python3
# Created by: Alex Kapajika
# Created on: Nov 11, 2023
# This program calculates the perimeter of a triangle with 3 sides
# And also tells you what type of triangle it is


def per_tri(sideA, sideB, sideC):
# Calculate the perimeter of the triangle
    perimeter = sideA + sideB + sideC
    print(f"Perimeter: {perimeter}cm")

    if sideA == sideB == sideC:
        print("This form a equilateral triangle")
# Check the type of triangle based on side lengths
    elif (
        sideA == sideB != sideC
        or sideC == sideA != sideB
        or sideB == sideC != sideA
        ):
            print("This form an isosceles triangle")
    elif sideA != sideB != sideC:
        print("This form a scalene triangle")



def main():
# Get user input for triangle sides
    user_sideA = input("Enter the sideA : ")
    user_sideB = input("Enter the sideB : ")
    user_sideC = input("Enter the sideC : ")

    try:
        user_sideA = float(user_sideA)
        user_sideB = float(user_sideB)
        user_sideC = float(user_sideC)
    except ValueError as e:
        print("{} Please enter a valid number(s).".format(e))

# Call the function
    else:
        per_tri(user_sideA, user_sideB, user_sideC)

if __name__ == "__main__":
    main()