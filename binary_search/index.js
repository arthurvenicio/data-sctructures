/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target, left = 0, rigth = null) {
  if (rigth == null) {
    rigth = nums.length;
  }

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

module.exports = search;
