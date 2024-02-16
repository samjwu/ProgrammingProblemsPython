class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = Counter(arr)

        freq = list(counts.values())

        freq.sort()

        removed = 0

        for i in range(len(freq)):
            removed += freq[i]

            if removed > k:
                return len(freq) - i

        return 0
