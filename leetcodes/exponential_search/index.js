const binarySearch = require("../binary_search");

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var exponentialSearch = function (nums, target) {
  if (nums[0] == target) {
    return 0;
  }

  let arrLength = nums.length; // number of total of items in array
  let right = 1; // created pointer with 1.

  while (right < arrLength && nums[right] < target) {
    // verify if the pointer is less then the array length, and if the number of the pointer is less than the target
    right = right * 2; // if the validation is true, ou double the right position.
  }

  if (nums[right] == target) {
    // if the number of the pointer is the target, return the pointer index.
    return right;
  }

  return binarySearch(
    // but if not the target, and the number of the pointer is greater than the target, we use a binary search
    nums,
    target,
    parseInt(right / 2),
    Math.min(right, arrLength - 1)
  );
};

console.log(
  exponentialSearch(
    [
      1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
      22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40
    ],
    32
  )
);
