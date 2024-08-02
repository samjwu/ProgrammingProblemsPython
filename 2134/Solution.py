class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        swap0 = self.calcMinSwaps(nums, 0)
        swap1 = self.calcMinSwaps(nums, 1)
        return min(swap0, swap1)

    def calcMinSwaps(self, data: List[int], val: int) -> int:
        n = len(data)

        countVal = 0

        for i in range(n - 1, -1, -1):
            if data[i] == val:
                countVal += 1

        if countVal == 0 or countVal == n:
            return 0

        start = 0
        end = 0

        maxValInWindow = 0
        currValInWindow = 0

        # window size must be at least the size of the count of value
        while end < countVal:
            if data[end] == val:
                currValInWindow += 1
            end += 1

        maxValInWindow = max(maxValInWindow, currValInWindow)

        # slide window by 1
        while end < n:
            if data[start] == val:
                currValInWindow -= 1
            start += 1

            if data[end] == val:
                currValInWindow += 1
            end += 1

            maxValInWindow = max(maxValInWindow, currValInWindow)

        return countVal - maxValInWindow
