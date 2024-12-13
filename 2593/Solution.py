class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        
        numsIndices = [(num, idx) for idx, num in enumerate(nums)]
        
        numsIndices.sort(key=lambda x: (x[0], x[1]))
        
        marked = [False] * n

        ans = 0

        for i in range(n):
            number = numsIndices[i][0]
            index = numsIndices[i][1]

            if not marked[index]:
                ans += number
                marked[index] = True

                if index - 1 >= 0:
                    marked[index - 1] = True
                if index + 1 < n:
                    marked[index + 1] = True

        return ans
