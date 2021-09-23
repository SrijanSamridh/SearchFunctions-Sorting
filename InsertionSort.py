from os import system


def speak(Audio):
    print(f"\n: {Audio}")
    system(f'say {Audio}')


def insertionSort(arr, n):
    # Your code goes here
    # Traverse through 1 to len(arr)
    for i in range(1, n):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


nums = [5, 3, 8, 6, 7, 2]
size = len(nums)
# print(f"After Sorting array {nums} we get {insertionSort(nums, size)}")
speak(f"After Sorting array {nums} we get {insertionSort(nums, size)}")
