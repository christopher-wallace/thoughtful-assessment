#!/usr/bin/env python3

import argparse

def sort(width, height, length, mass):
    volume = width * height * length
    heavy = mass >= 20
    bulky = width >= 150 or height >= 150 or length >= 150 or volume >= 1000000

    if heavy and bulky:
        return "REJECTED"
    elif heavy or bulky:
        return "SPECIAL"
    else:
        return "STANDARD"

def positive_int(value):
    try:
        ivalue = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"{value} is not an integer")

    if ivalue <= 0:
        raise argparse.ArgumentTypeError("Value must be a positive integer")

    return ivalue

def main():
    parser = argparse.ArgumentParser(
        description="Calculates package type based on height, width, length, and mass."
    )

    parser.add_argument(
        "--width",
        type=positive_int,
        required=True,
        help="Width of package in cm"
    )

    parser.add_argument(
        "--height",
        type=positive_int,
        required=True,
        help="Height of package in cm"
    )

    parser.add_argument(
        "--length",
        type=positive_int,
        required=True,
        help="Length of package in cm"
    )

    parser.add_argument(
        "--mass",
        type=positive_int,
        required=True,
        help="Mass of package in kg"
    )

    args = parser.parse_args()

    print(f"Put the specified package in the {sort(args.width, args.height, args.length, args.mass)} stack.")

if __name__ == "__main__":
    main()
