#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#


# @lc code=start
class Solution:
    def trap(self, height: list[int]) -> int:
        forward_pt, backward_pt = 1, 0
        total_water = 0
        while backward_pt < len(height) - 1:
            max_height_index, max_height = 0, 0
            while forward_pt < len(height):
                if height[forward_pt] > height[backward_pt]:
                    first_height = height[backward_pt]
                    backward_pt += 1
                    while backward_pt < forward_pt:
                        total_water += first_height - height[backward_pt]
                        backward_pt += 1
                    break
                if height[forward_pt] >= max_height:
                    max_height = height[forward_pt]
                    max_height_index = forward_pt
                forward_pt += 1
            else:
                forward_pt = max_height_index
                backward_pt += 1
                while backward_pt < forward_pt:
                    total_water += max_height - height[backward_pt]
                    backward_pt += 1
            forward_pt = backward_pt + 1
        return total_water


# @lc code=end
print(
    f"Output: {Solution().trap([6, 5, 4, 3, 0, 0, 0, 7, 3, 2, 1, 4])}, Correct output: 30"
)
print(f"Output: {Solution().trap([0, 7, 1, 4, 6])}, Correct output: 7")
print(f"Output: {Solution().trap([4, 2, 0, 3, 2, 4, 3, 4])}, Correct output: 10")
print(
    f"Output: {Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])}, Correct output: 6"
)
print(f"Output: {Solution().trap([4, 2, 3])}, Correct output: 1")
print(f"Output: {Solution().trap([4, 2, 0, 0, 3])}, Correct output: 7")
print(f"Output: {Solution().trap([5, 2, 0, 0, 4])}, Correct output: 10")
