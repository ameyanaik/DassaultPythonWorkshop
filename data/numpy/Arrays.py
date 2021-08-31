import numpy as np

# This is a 1 Dimensional array
arr1 = np.array([1, 2, 3, 4, 5, 6])

# This is a 2 Dimensional array - like a table
arr2 = np.array([['a', 'b', 'c'], [1, 2, 3], ['#', '$', '%']])

# This is a 3 Dimensional array
arr3 = np.array([[['a', 'b', 'c'], [1, 2, 3], ['#', '$', '%']], [['x', 'y', 'z'], [24, 25, 26], ['^', '&', '*']]])

# This is a 5 Dimensional array
arr5 = np.array([1, 2, 3, 4], ndmin=5)

def main():
    print("arr1:", arr1)
    print("arr2:\n", arr2)
    print("arr3:\n", arr3)
    print("arr5:\n", arr5)
    print("No of dimensions are:", arr5.ndim)


if __name__ == "__main__":
    main()
