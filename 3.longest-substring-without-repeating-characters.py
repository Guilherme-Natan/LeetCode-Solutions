#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#


# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        char_set = set(s[0])
        lp, rp = 0, 1
        sequence = 0
        while rp < len(s):
            while s[rp] in char_set:
                sequence = max(sequence, rp - lp)
                char_set.remove(s[lp])
                lp += 1
            char_set.add(s[rp])
            rp += 1
        return max(sequence, rp - lp)


# @lc code=end
