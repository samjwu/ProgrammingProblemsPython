class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        n = len(s)

        diffs = [0] * n

        for shift in shifts:
            if shift[2] == 1:
                diffs[shift[0]] += 1

                if shift[1] + 1 < n:
                    diffs[shift[1] + 1] -= 1
            else:
                diffs[shift[0]] -= 1

                if shift[1] + 1 < n:
                    diffs[shift[1] + 1] += 1

        ans = list(s)
        shift_vector = 0

        for i in range(n):
            shift_vector = (shift_vector + diffs[i]) % 26
            if shift_vector < 0:
                shift_vector += 26

            shifted_char = chr((ord(s[i]) - ord("a") + shift_vector) % 26 + ord("a"))
            ans[i] = shifted_char

        return "".join(ans)
