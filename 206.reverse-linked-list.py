#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # Iteratively
    def reverseList(self, head):
        prv = None
        while head:
            nxt = head.next
            head.next = prv
            prv = head
            head = nxt
        return prv


# @lc code=end
