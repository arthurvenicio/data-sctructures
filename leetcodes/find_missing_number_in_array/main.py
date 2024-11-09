def missingNumber(nums):
    x = 0

    for num in nums:
        x ^= num

    for i in range(len(nums) + 1):
        x ^= i
    return x


arr = missingNumber([3,0,1])

print(arr)