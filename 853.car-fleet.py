#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#


# @lc code=start
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pos_spd = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        fleet_stack = []
        for pos, spd in pos_spd:
            if not fleet_stack:
                fleet_stack.append((pos, spd))
                continue
            pos_stk, spd_stk = fleet_stack.pop()
            t = (pos - pos_stk) / (spd_stk - spd) if spd_stk != spd else -1
            if t < 0 or pos + spd * t > target:  # Not a fleet
                fleet_stack.append((pos_stk, spd_stk))
                fleet_stack.append((pos, spd))
                continue
            fleet_stack.append((pos_stk, spd_stk))

        return len(fleet_stack)


# @lc code=end
target_in = 13
position_in = [10, 2, 5, 7, 4, 6, 11]
speed_in = [7, 5, 10, 5, 9, 4, 1]
a = Solution().carFleet(target_in, position_in, speed_in)
print(a)
