#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#


# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) - 1
        while R >= L:
            M = (L + R) // 2
            if nums[M] < min(nums[L], nums[R]):
                R = M
            elif nums[L] > nums[R]:
                L = M + 1
            else:
                R = M - 1
        return nums[L]


# @lc code=end
