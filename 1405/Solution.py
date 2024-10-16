class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []

        if a > 0:
            heapq.heappush(maxHeap, (-a, 'a'))
        if b > 0:
            heapq.heappush(maxHeap, (-b, 'b'))
        if c > 0:
            heapq.heappush(maxHeap, (-c, 'c'))

        heapq.heapify(maxHeap)

        ans = []

        while maxHeap:
            freq, c = heapq.heappop(maxHeap)

            if len(ans) >= 2 and ans[-1] == ans[-2] == c:
                if not maxHeap:
                    break

                freq2, c2 = heapq.heappop(maxHeap)
                ans.append(c2)

                if freq2 + 1 < 0:
                    heapq.heappush(maxHeap, (freq2 + 1, c2))

                heapq.heappush(maxHeap, (freq, c))
            else:
                ans.append(c)

                if freq + 1 < 0:
                    heapq.heappush(maxHeap, (freq + 1, c))

        return "".join(ans)
