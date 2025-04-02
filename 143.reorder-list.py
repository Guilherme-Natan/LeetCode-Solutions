#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head):
        # This solution has a space complexity of O(n), while the optimal one has O(1)
        tail = head
        stack = []
        while tail.next:
            stack.append(tail)
            tail = tail.next

        middle = head
        while middle.next and middle.next.next:
            tail.next = middle.next
            middle.next = tail
            tail = stack.pop()
            tail.next = None
            middle = middle.next.next


# @lc code=end
