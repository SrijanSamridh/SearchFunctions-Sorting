            # SELECTION SORT

nums = [5, 3, 8, 6, 7, 2]
def SelectionSort(nums):
    for i in range(len(nums)):
        minpos = i
        for j in range(i, len(nums)):
            if nums[j] < nums[minpos]:
                minpos = j
        arr[i],arr[min_pos] = arr[min_pos], arr[i]

    # print(nums)

SelectionSort(nums)
print(nums)
