def hammingWeight(n: int) -> int:
    counter = 0

    while n != 0:
        n &= (n - 1) # clear the least significant bit set
        counter +=1

    return counter

