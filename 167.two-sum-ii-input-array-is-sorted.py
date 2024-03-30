#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#


# @lc code=start
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        lp, rp = 0, len(numbers) - 1
        while True:
            targ_sum = numbers[lp] + numbers[rp]
            if targ_sum < target:
                lp += 1
                continue
            if targ_sum > target:
                rp -= 1
                continue
            return [lp + 1, rp + 1]


# @lc code=end
