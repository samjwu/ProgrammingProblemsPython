class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)

        ans = 0
        decrement = 0

        for i in range(k):
            ans += max(happiness[i] - decrement, 0)
            decrement += 1

        return ans
