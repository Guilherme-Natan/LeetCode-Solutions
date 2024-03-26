#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        count_map = defaultdict(list)
        for string in strs:
            count_map[tuple(sorted(string))].append(string)
        return count_map.values()


# @lc code=end
