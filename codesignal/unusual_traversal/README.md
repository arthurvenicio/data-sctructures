## Question

You are provided with an array of n integers, where n ranges from **1** to **501** and is always an odd number. The elements of the array span values from `-10⁶` to `10⁶`, inclusive. The goal is to return a new array constructed by traversing the initial array in a specific order, outlined as follows:

Begin with the middle element of the array.
For each subsequent pair of elements, alternate between taking two elements from the left and two elements from the right, relative to the middle.
If fewer than two elements remain on either side, include all the remaining elements from that side.
Continue this process until all elements of the array have been traversed.
For example, for `array = [1, 2, 3, 4, 5, 6, 7]`, your function should return `[4, 2, 3, 5, 6, 1, 7]`. And for array = `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]`, your function should return `[6, 4, 5, 7, 8, 2, 3, 9, 10, 1, 11]`.
