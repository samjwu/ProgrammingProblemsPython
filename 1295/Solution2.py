class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        def is_even_digits(num: int) -> bool:
            count = 0

            while num:
                num = num // 10
                count += 1

            return count % 2 == 0

        ans = 0

        for num in nums:
            if is_even_digits(num):
                ans += 1

        return ans
