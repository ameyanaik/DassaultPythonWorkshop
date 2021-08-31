from data.numpy.Arrays import arr1, arr2

def main():
    # Copy
    c1 = arr1.copy()
    print(c1)

    c1[3] = 9

    print("Original Array:", arr1)
    print("Copied Array:", c1)

    #View
    v1 = arr1.view()
    v1[3] = 9
    print("Original Array:", arr1)
    print("Copied Array:", v1)

    #Slice an Array and store it in new variable

    s1 = arr1[-2:]
    print(s1)

    s2 = arr2[:2, -2:]
    print(s2)

if __name__ == "__main__":
    main()