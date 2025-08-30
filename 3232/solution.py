from typing import list


class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        singles = 0
        doubles = 0

        for num in nums:
            if num >= 10:
                doubles += num
            else:
                singles += num

        return True if singles > doubles or doubles > singles else False
