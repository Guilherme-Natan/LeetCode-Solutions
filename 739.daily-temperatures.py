#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#


# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        days_warmer = [0] * len(temperatures)
        days_stack = []
        for i, temp in enumerate(temperatures):
            while days_stack and temp > days_stack[-1][1]:
                i_stk, _ = days_stack.pop()
                days_warmer[i_stk] = i - i_stk
            days_stack.append((i, temp))
        return days_warmer


# @lc code=end
inp = [
    64,
    40,
    49,
    73,
    72,
    35,
    68,
    83,
    35,
    73,
    84,
    88,
    96,
    43,
    74,
    63,
    41,
    95,
    48,
    46,
    89,
    72,
    34,
    85,
    72,
    59,
    87,
    49,
    30,
    32,
    47,
    34,
    74,
    58,
    31,
    75,
    73,
    88,
    64,
    92,
    83,
    64,
    100,
    99,
    81,
    41,
    48,
    83,
    96,
    92,
    82,
    32,
    35,
    68,
    68,
    92,
    73,
    92,
    52,
    33,
    44,
    38,
    47,
    88,
    71,
    50,
    57,
    95,
    33,
    65,
    94,
    44,
    47,
    79,
    41,
    74,
    50,
    67,
    97,
    31,
    68,
    50,
    37,
    70,
    77,
    55,
    48,
    30,
    77,
    100,
    31,
    100,
    69,
    60,
    47,
    95,
    68,
    47,
    33,
    64,
]
a = Solution().dailyTemperatures(inp)
print(a)
