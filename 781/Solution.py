class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = {}
        ans = 0

        for a in answers:
            if a == 0:
                ans += 1
            else:
                if a not in freq or a == freq[a]:
                    freq[a] = 0
                    ans += a + 1
                else:
                    freq[a] += 1

        return ans
