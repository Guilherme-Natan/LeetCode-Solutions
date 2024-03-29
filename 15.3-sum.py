#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#


# @lc code=start
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        solutions = []
        previous_target = None

        while len(nums) >= 3:
            target = nums.pop()
            if target == previous_target:
                continue
            previous_target = target

            lp, rp = 0, len(nums) - 1
            while rp > lp:
                zero_sum = nums[lp] + nums[rp] + target
                if zero_sum == 0:
                    if not solutions or (nums[lp], nums[rp]) != (
                        solutions[-1][0],
                        solutions[-1][1],
                    ):
                        solutions.append([nums[lp], nums[rp], target])
                    else:
                        lp += 1
                    continue
                if zero_sum > 0:
                    rp -= 1
                    continue
                if zero_sum < 0:
                    lp += 1

        return solutions


# @lc code=end

print(Solution().threeSum([0, 0, 0, 0]))
