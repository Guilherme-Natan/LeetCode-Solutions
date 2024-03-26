#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#


# @lc code=start
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        first_set = set(nums)
        final_set = set(nums)
        for n in nums:
            if n in first_set:
                first_set.remove(n)
            else:
                final_set.remove(n)

        return final_set.pop()


# @lc code=end
