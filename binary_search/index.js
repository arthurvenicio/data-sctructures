/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
  let left = 0;
  let rigth = nums.length;

  while (left < rigth) {
    let mid = parseInt((left + rigth) / 2);

    if (nums[mid] === target) {
      return mid;
    }

    if (nums[mid] < target) {
      left = mid + 1;
    } else {
      rigth = mid;
    }
  }

  return -1;
};

console.log(search([-1, 0, 3, 5, 9, 12], 9));
