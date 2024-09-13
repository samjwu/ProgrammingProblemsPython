class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        
        prefix = [0 for i in range(n+1)]
        
        for i in range(n):
            prefix[i+1] = prefix[i] ^ arr[i]
        
        ans = []
        
        for q in queries:
            ans.append(prefix[q[1] + 1] ^ prefix[q[0]])
        
        return ans
