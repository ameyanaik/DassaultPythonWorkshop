from data.numpy.Arrays import arr1, arr2, arr3, arr5


def main():
    print(arr1[0])

    # Access the last element of arr1
    print(arr1[-1])

    # Access Row2 and Column2 from arr2
    print(arr2[1, 1])

    # Access Table 2, Row 3, Column 1 from arr3
    print(arr3[1, 2, 0])

    # Access Table 1, Row 4, Column 3 from arr3
    try:
        print(arr3[0, 3, 2])
    except IndexError as e:
        print("The element you are trying to access is out of bounds")
        print(e)


if __name__ == "__main__":
    main()
