const backtrack = (
  nums: number[],
  i: number,
  res: number[][],
  sol: number[]
) => {
  if (i == nums.length) {
    res.push([...sol]);
    return;
  }

  // Don't puck nums[i]
  backtrack(nums, i + 1, res, sol);

  sol.push(nums[i]);
  // Now pick nums[i]
  backtrack(nums, i + 1, res, sol);
  sol.pop();
};

function subsets(nums: number[]): number[][] {
  let res = [];
  let sol = [];
  backtrack(nums, 0, res, sol);
  return res;
}
