#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        fp = sp = head

        while fp and fp.next:
            fp = fp.next.next
            sp = sp.next
            if fp == sp:
                return True
        return False


# @lc code=end
