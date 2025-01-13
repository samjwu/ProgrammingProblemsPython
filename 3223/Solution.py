class Solution:
    def minimumLength(self, s: str) -> int:
        deques = [deque() for i in range(26)]

        skipped = 0
        
        n = len(s)

        for i in range(n):
            order = ord(s[i]) - ord('a')
            deques[order].append(i)

            if len(deques[order]) > 2:
                deques[order].popleft()
                deques[order].pop()
                skipped += 2

        return n - skipped
