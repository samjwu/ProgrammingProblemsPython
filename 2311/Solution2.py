class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        answer_length = 0
        current_value = 0
        # answer is capped by max number of bits in k
        # alternative: len(bin(k)) - 2
        max_bits = k.bit_length()

        # traverse backwards from LSB to MSB
        for i, c in enumerate(s[::-1]):
            if c == "1":
                # include 1 bit if it will not exceed k
                if i < max_bits and current_value + (1 << i) <= k:
                    current_value += 1 << i
                    answer_length += 1
            else:
                # include 0 bit since adding zeroes will never exceed k
                answer_length += 1

        return answer_length
