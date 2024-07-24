class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        n = len(nums)

        # store tuple of mapped value and index
        pairs = []

        for i in range(n):
            s = str(nums[i])

            converted = ""

            for j in range(len(s)):
                converted += str(mapping[int(s[j])])
            
            mapped = int(converted)
            
            pairs.append((mapped, i))

        pairs.sort()

        ans = []

        for pair in pairs:
            ans.append(nums[pair[1]])
            
        return ans
