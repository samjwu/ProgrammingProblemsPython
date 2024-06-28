class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree = [0 for i in range(n)]

        for road in roads:
            degree[road[0]] += 1
            degree[road[1]] += 1

        degree.sort()

        ans = 0
        
        importance = 1
        
        for city in degree:
            ans += city * importance
            importance += 1

        return ans
