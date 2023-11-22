class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        m = len(nums)

        diagonals = defaultdict(list)
        
        for row in range(m-1, -1, -1):
            for col in range(len(nums[row])):
                diagonals[row + col].append(nums[row][col])
                
        ans = []
        diagonal = 0
        
        while diagonal in diagonals:
            ans.extend(diagonals[diagonal])
            diagonal += 1

        return ans
