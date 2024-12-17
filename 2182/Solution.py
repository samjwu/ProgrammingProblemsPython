class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = defaultdict(int)
        
        for c in s:
            freq[c] += 1
            
        maxHeap = []
        
        for c in freq.keys():
            heapq.heappush(maxHeap, (-ord(c), freq[c]))
                
        ans = []
        
        while maxHeap:
            order, count = heapq.heappop(maxHeap)
            c = chr(-order)
            repeat = min(count, repeatLimit)
            ans.append(c * repeat)
            
            if count > repeat and maxHeap:
                order2, count2 = heapq.heappop(maxHeap)
                c2 = chr(-order2)
                ans.append(c2)
                
                if count2 > 1:
                    heapq.heappush(maxHeap, (order2, count2 - 1))
                heapq.heappush(maxHeap, (order, count - repeat))
                
        return "".join(ans)
