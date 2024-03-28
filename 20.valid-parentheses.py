#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#


# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {")": "(", "]": "[", "}": "{"}
        bracket_stack = []
        for bracket in s:
            if bracket in bracket_map:
                if bracket_stack and bracket_map[bracket] == bracket_stack[-1]:
                    bracket_stack.pop()
                    continue
                return False
            bracket_stack.append(bracket)

        if len(bracket_stack) > 0:
            return False
        return True


# @lc code=end
