#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#


# @lc code=start
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        vertical_lines = [set() for _ in range(9)]
        horizontal_lines = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if (
                    board[i][j] in vertical_lines[j]
                    or board[i][j] in horizontal_lines[i]
                    or board[i][j] in squares[3 * (i // 3) + (j // 3)]
                ):
                    return False
                if board[i][j] != ".":
                    vertical_lines[j].add(board[i][j])
                    horizontal_lines[i].add(board[i][j])
                    squares[3 * (i // 3) + (j // 3)].add(board[i][j])

        return True


# @lc code=end

test1 = [
    [".", "8", "7", "6", "5", "4", "3", "2", "1"],
    ["2", ".", ".", ".", ".", ".", ".", ".", "."],
    ["3", ".", ".", ".", ".", ".", ".", ".", "."],
    ["4", ".", ".", ".", ".", ".", ".", ".", "."],
    ["5", ".", ".", ".", ".", ".", ".", ".", "."],
    ["6", ".", ".", ".", ".", ".", ".", ".", "."],
    ["7", ".", ".", ".", ".", ".", ".", ".", "."],
    ["8", ".", ".", ".", ".", ".", ".", ".", "."],
    ["9", ".", ".", ".", ".", ".", ".", ".", "."],
]
solution1 = Solution().isValidSudoku(board=test1)
print(solution1)
