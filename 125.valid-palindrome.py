#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#


# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lp, rp = 0, len(s) - 1
        while rp > lp:
            while not s[rp].isalnum():
                rp -= 1
                if rp == 0:
                    return True
            while not s[lp].isalnum():
                lp += 1
                if lp == len(s) - 1:
                    return True
            if s[rp].lower() != s[lp].lower():
                return False
            rp -= 1
            lp += 1
        return True


# @lc code=end

print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution().isPalindrome("race a car"))
print(Solution().isPalindrome(" "))
print(Solution().isPalindrome(".,"))
