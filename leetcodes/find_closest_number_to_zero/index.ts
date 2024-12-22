function findClosestNumber(nums: number[]): number {
  let closest = nums[0];

  for (const num of nums) {
    if (Math.abs(num) < Math.abs(closest)) {
      closest = num;
    }
  }

  if (closest < 0 && nums.indexOf(Math.abs(closest)) > 0) {
    return Math.abs(closest);
  }

  return closest;
}
