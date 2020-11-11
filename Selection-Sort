            # SELECTION SORT

nums = [5, 3, 8, 6, 7, 2]
def SelectionSort(nums):
    for i in range(len(nums)):
        minpos = i
        for j in range(i, len(nums)):
            if nums[j] < nums[minpos]:
                minpos = j
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

        # print(nums)

SelectionSort(nums)
print(nums)
