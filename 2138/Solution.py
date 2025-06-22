from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        substrings = []
        n = len(s)

        for i in range(0, n, k):
            substring = s[i:i+k]
            substrings.append(substring)

        last_length = len(substrings[-1])
        if last_length != k:
            diff = k - last_length
            substrings[-1] = substrings[-1] + fill * diff

        return substrings
