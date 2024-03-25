#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#


# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        countain_set = set()

        for n in nums:
            if n in countain_set:
                return True
            countain_set.add(n)

        return False


# @lc code=end
