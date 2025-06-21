from collections import defaultdict

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = defaultdict(int)

        for c in word:
            freq[c] += 1

        min_removed = len(word)

        for base_count in freq.values():
            removed = 0

            for compare_count in freq.values():
                if base_count > compare_count:
                    # remove all of compared char
                    # since cannot raise count of compared char
                    removed += compare_count
                elif compare_count > base_count + k:
                    # reduce compared char
                    # to match base char plus k
                    removed += compare_count - (base_count + k)

            min_removed = min(min_removed, removed)

        return min_removed
