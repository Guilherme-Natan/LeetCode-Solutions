#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#


# @lc code=start
# Not exactly O(1), but it seems to be on average O(1)
from collections import defaultdict


class MinStack:

    def __init__(self):
        self.minstack = []
        self.min_number = 21474836460
        self.min_hashmap = defaultdict(list)

    def push(self, val: int) -> None:
        self.minstack.append(val)
        if self.min_number >= val:
            self.min_hashmap[val].append(self.min_number)
            self.min_number = val

    def pop(self) -> None:
        removed_num = self.minstack.pop()
        if removed_num == self.min_number:
            self.min_number = min(self.min_hashmap[removed_num])
            self.min_hashmap[removed_num].remove(self.min_number)

    def top(self) -> int:
        top = self.minstack[-1]
        return top

    def getMin(self) -> int:
        return self.min_number


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end
