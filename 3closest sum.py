Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104


class Solution:
  def threeSumClosest(self, nums: List[int], target: int) -> int:
    ans = nums[0] + nums[1] + nums[2]

    nums.sort()

    for i in range(len(nums) - 2):
      if i > 0 and nums[i] == nums[i - 1]:
        continue
      # Choose nums[i] as the first number in the triplet, then search the
      # remaining numbers in [i + 1, n - 1].
      l = i + 1
      r = len(nums) - 1
      while l < r:
        summ = nums[i] + nums[l] + nums[r]
        if summ == target:
          return summ
        if abs(summ - target) < abs(ans - target):
          ans = summ
        if summ < target:
          l += 1
        else:
          r -= 1

    return ans
