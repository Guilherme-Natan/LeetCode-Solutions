#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#


# @lc code=start
class Solution:
    def maxArea(self, height: list[int]) -> int:
        lp, rp = 0, len(height) - 1
        max_area = 0
        while rp > lp:
            water_area = (rp - lp) * min(height[lp], height[rp])
            if water_area > max_area:
                max_area = water_area
            if height[rp] > height[lp]:
                lp += 1
            else:
                rp -= 1
        return max_area


# @lc code=end
