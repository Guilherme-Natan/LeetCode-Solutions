#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#


# @lc code=start
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set(nums)
        max_sequence = 0
        for n in nums:
            if n - 1 not in nums_set:
                sequence = 1
                n += 1
                while n in nums_set:
                    n += 1
                    sequence += 1
                max_sequence = max(max_sequence, sequence)

        return max_sequence


# @lc code=end
