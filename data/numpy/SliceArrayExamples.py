from data.numpy.Arrays import arr1, arr2, arr3, arr5

def main():
    # Slice 1 D Array
    # Get a slice of arr1 from position 1 to 5
    print("Slice of arr1 from position 1 to 5:", arr1[0:5])
    # Get all elements from position 3 onwards
    print("Elements from position 3 onwards:", arr1[2:])
    print("Elements up to position 4", arr1[:4])
    print("All alternate elements", arr1[::2])

    # Slice 2 D Array
    print("Elements in row 2 only from columns 2 and 3:", arr2[1, 1:3])
    print("From all 3 rows, return column 1", arr2[0:3, 0])
    print("From all 3 rows, return column 1", arr2[0:, 0])
    print("From all 3 rows, return column 1", arr2[:3, 0])
    print("From first 2 rows, return last 2 columns", arr2[0:2, 1:3])
    print("From first 2 rows, return last 2 columns", arr2[:2, -2:])

    # Slice a 3 D Array
    #print("From Table 2, get first 2 rows and first column", arr3[:2, :3, :1])
    print("From Table 2, get first 2 rows and first column", arr3[1, :2, 0])
    print("From both tables, get first row and last column", arr3[:, 0, -1])
    print("From all tables, get last 2 rows and first 2 columns\n", arr3[:, -2:, :2])
    print("From all tables, get first column\n", arr3[:, :, 0])



if __name__ == "__main__":
        main()
