class UnionFind:
    def __init__(self, n: int):
        self.parents = [i for i in range(n)]
    
    def find(self, x: int) -> int:
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
            
        return self.parents[x]

    def unify(self, x: int, y: int) -> bool:
        parentX = self.find(x)
        parentY = self.find(y)
        
        if parentX == parentY:
            return False
        
        self.parents[parentX] = parentY
        return True

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        ans = 0
        aliceReach = 0
        bobReach = 0

        # Alice and Bob
        aliceGraph = UnionFind(n+1)
        bobGraph = UnionFind(n+1)
        for edgeType, u, v in edges:
            if edgeType == 3:
                if aliceGraph.unify(u, v) and bobGraph.unify(u, v):
                    aliceReach += 1
                    bobReach += 1
                else:
                    ans += 1
        
        for edgeType, u, v in edges:
            if edgeType == 1:
                if aliceGraph.unify(u, v):
                    aliceReach += 1
                else:
                    ans += 1
                    
        for edgeType, u, v in edges:
            if edgeType == 2:
                if bobGraph.unify(u, v):
                    bobReach += 1
                else:
                    ans += 1
        
        if aliceReach == n-1 and bobReach == n-1:
            return ans
        return -1
