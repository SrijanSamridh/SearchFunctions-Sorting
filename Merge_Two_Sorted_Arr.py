# Merge arr1[0..n1-1] and
# arr2[0..n2-1] into
# arr3[0..n1+n2-1]
def mergeArrays(arr1, n, arr2, m):
    i = 0
    j = 0
    arr3 = []

    # Traverse both array
    while i < n and j < m:

        # Check if current element
        # of first array is smaller
        # than current element of
        # second array. If yes,
        # store first array element
        # and increment first array
        # index. Otherwise do same
        # with second array
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i = i + 1
        else:
            arr3.append(arr2[j])
            j = j + 1

    # Store remaining elements
    # of first array
    while i < n:
        arr3.append(arr1[i])
        i = i + 1

    # Store remaining elements
    # of second array
    while j < m:
        arr3.append(arr2[j])
        j = j + 1

    print("Array after merging")
    for i in range(n + m):
        print(str(arr3[i]), end=" ")
    # return arr3


# Driver code
arr1 = [1, 3, 5, 7, 13]
n1 = len(arr1)

arr2 = [2, 4, 6, 8]
n2 = len(arr2)
mergeArrays(arr1, n1, arr2, n2)
