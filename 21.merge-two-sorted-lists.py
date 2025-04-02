#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def mergeTwoLists(self, list1, list2):
    head = tail = ListNode()
    while list1 or list2:
        if not list2 or (list1 and list1.val <= list2.val):
            tail.next = ListNode(list1.val)
            list1 = list1.next
        else:
            tail.next = ListNode(list2.val)
            list2 = list2.next
        tail = tail.next
    return head.next


# @lc code=end
