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


# arr = [1,2,5,4,3]
# arrS = bubble(arr)
# print(arrS)

# we must compare consecutive items, and validate if it is in the correct place ex: arr[left] < arr[right]. The higher value, is bubble to most right possible

# The worst case time complexy is : O(n²)

# divide and conquer