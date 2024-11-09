def bubble(nums):
    size = len(nums)

    for _ in nums:
        swapped = False
        print(nums)
        for j in range(size-1):
            if nums[j] > nums[j+1]:
                nums[j+1], nums[j] = nums[j], nums[j+1]
                swapped = True
        if swapped is False:
            break

    return nums


arr = [1,2,5,4,3]
arrS = bubble(arr)
# print(arrS)