class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        freq_a = defaultdict(int)
        freq_b = defaultdict(int)
        freq_ab = defaultdict(int)

        for i in range(n):
            freq_a[tops[i]] += 1
            freq_b[bottoms[i]] += 1
            if tops[i] == bottoms[i]:
                freq_ab[tops[i]] += 1

        for i in range(1, 7):
            if freq_a[i] + freq_b[i] - freq_ab[i] >= n:
                return n - max(freq_a[i], freq_b[i])

        return -1
