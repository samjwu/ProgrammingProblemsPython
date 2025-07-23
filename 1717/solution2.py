class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        max_gain = 0
        chars = list(s)

        # greedy: remove higher scoring substring first
        if x > y:
            hi = "ab"
            lo = "ba"
        else:
            hi = "ba"
            lo = "ab"

        max_gain += self.remove_substr(chars, hi, max(x, y))
        max_gain += self.remove_substr(chars, lo, min(x, y))

        return max_gain

    def remove_substr(self, chars: list[str], pair: str, points: int) -> int:
        gain = 0
        write_idx = 0

        for read_idx in range(len(chars)):
            chars[write_idx] = chars[read_idx]
            write_idx += 1

            if write_idx > 1 and chars[write_idx-2] == pair[0] and chars[write_idx-1] == pair[1]:
                write_idx -= 2
                gain += points

        del chars[write_idx:]

        return gain
