#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#


# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        k_min = 1
        k_max = max(piles)
        while k_max >= k_min:
            k = (k_min + k_max) // 2
            h_test = sum(math.ceil(i / k) for i in piles)
            if h_test <= h:
                k_max = k - 1
            elif h_test > h:
                k_min = k + 1
        return k_min


# @lc code=end


print(Solution().minEatingSpeed([312884470], 312884469))
# print(Solution().minEatingSpeed([3, 6, 7, 11], 8))
