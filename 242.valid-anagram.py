#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#


# @lc code=start
from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s = defaultdict(int)
        count_t = defaultdict(int)

        for s_letter, t_letter in zip(s, t):
            count_s[s_letter] += 1
            count_t[t_letter] += 1

        if count_s != count_t:
            return False
        return True


# @lc code=end
