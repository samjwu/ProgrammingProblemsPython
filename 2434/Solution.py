from collections import Counter

class Solution:
    def robotWithString(self, s: str) -> str:
        freq = Counter(s)
        stack = []
        lex_smallest = []
        # smallest character remaining in freq
        min_char_remaining = "a"

        for c in s:
            stack.append(c)
            freq[c] -= 1
            
            # find next minimum character in freq
            while min_char_remaining != "z" and freq[min_char_remaining] == 0:
                min_char_remaining = chr(ord(min_char_remaining) + 1)

            # write characters smaller than the minimal in freq
            while stack and stack[-1] <= min_char_remaining:
                lex_smallest.append(stack.pop())

        return "".join(lex_smallest)
