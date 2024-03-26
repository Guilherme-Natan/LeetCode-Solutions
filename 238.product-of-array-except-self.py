#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#


# @lc code=start
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        product_list = [1] * len(nums)
        prefix = 1
        for i, n in enumerate(nums):
            product_list[i] = prefix
            prefix *= n
        postfix = 1
        for i in range(-len(nums) - 1, -1, -1):
            product_list[i] *= postfix
            postfix *= nums[i]
        return product_list


# @lc code=end

test1 = [1, 2, 3, 4]
test2 = [-1, 1, 0, -3, 3]
solution1 = Solution().productExceptSelf(nums=test1)
solution2 = Solution().productExceptSelf(nums=test2)
print(solution1)
print(solution2)
