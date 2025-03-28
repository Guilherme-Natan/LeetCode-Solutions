# @lc code=start
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        low = 0
        high = len(matrix) * len(matrix[0]) - 1
        # matrix[outer_mid][inner_mid]
        while low <= high:
            mid = (low + high) // 2
            outer_mid, inner_mid = divmod(mid, len(matrix[0]))
            if matrix[outer_mid][inner_mid] < target:
                low = mid + 1
            elif matrix[outer_mid][inner_mid] > target:
                high = mid - 1
            else:
                return True
        return False


# @lc code=end
