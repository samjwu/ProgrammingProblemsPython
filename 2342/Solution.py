class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # map digit sum to min heap of actual
        digit_map = {}

        def calc_digit_sum(num):
            digits = 0

            while num > 0:
                digits += num % 10
                num //= 10

            return digits

        for num in nums:
            digit_sum = calc_digit_sum(num)

            if digit_sum not in digit_map:
                digit_map[digit_sum] = [num]
            else:
                heapq.heappush(digit_map[digit_sum], num)
                while len(digit_map[digit_sum]) > 2:
                    heapq.heappop(digit_map[digit_sum])

        ans = -1

        for digit_sum in digit_map:
            if len(digit_map[digit_sum]) != 2:
                continue
            
            candidate = digit_map[digit_sum][0] + digit_map[digit_sum][1]
            ans = max(ans, candidate)

        return ans

