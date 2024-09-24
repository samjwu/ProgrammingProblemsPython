class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr1Prefixes = set()

        for num in arr1:
            while num not in arr1Prefixes and num > 0:
                arr1Prefixes.add(num)
                num //= 10

        ans = 0

        for num in arr2:
            while num not in arr1Prefixes and num > 0:
                num //= 10

            if num > 0:
                ans = max(ans, len(str(num)))

        return ans
