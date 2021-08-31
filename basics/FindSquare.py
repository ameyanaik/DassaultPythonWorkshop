import argparse


def get_square(n):
    return n*n


parser = argparse.ArgumentParser()
parser.add_argument("num", help="Enter the number you want to find the square for")

args = parser.parse_args()

print(f"Square of the number {args.num} is:", get_square(int(args.num)))

