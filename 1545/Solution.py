class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        ans = "0"

        for i in range(1, n):
            if k <= len(ans):
                break

            ans += "1"

            inverted = "".join("1" if bit == "0" else "0" for bit in ans[:-1])
            ans += inverted[::-1]

        return ans[k - 1]
