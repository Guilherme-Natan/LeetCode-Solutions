#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#


# @lc code=start
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        token_stack = []
        symbol_to_op = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y),
        }
        for token in tokens:
            if token in symbol_to_op:
                y = token_stack.pop()
                x = token_stack.pop()
                token = symbol_to_op[token](int(x), int(y))
            token_stack.append(token)

        return int(token_stack.pop())


# @lc code=end

i = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
o = Solution().evalRPN(tokens=i)
print(o)
