class Solution:
    def frequencySort(self, s: str) -> str:
        freq = defaultdict(int)
        
        for c in s:
            freq[c] += 1
            
        maxHeap = []
        
        for c in freq.keys():
            # Python heap is min heap by default
            heapq.heappush(maxHeap, (-freq[c], c))
            
        ans = ""    
        
        while len(maxHeap) > 0:
            pair = heapq.heappop(maxHeap)
            
            ans += pair[1] * -pair[0]
            
        return ans
