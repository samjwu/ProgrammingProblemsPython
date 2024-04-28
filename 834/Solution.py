class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        self.n = n
        
        self.ans = [0 for i in range(n)]
        
        # count of number of nodes in the subtree at ith node
        self.count = [1 for i in range(n)]
        
        self.graph = [[] for i in range(n)]
        
        for edge in edges:
            self.graph[edge[0]].append(edge[1])
            
            # must do this 
            # since there is no guarantee that edge[0] < edge[1]
            self.graph[edge[1]].append(edge[0])
            
        self.dfs(0, -1)
        
        self.dfs2(0, -1)
        
        return self.ans
    
    def dfs(self, node: int, parent: int) -> None:
        """
        Calculate the correct distances at the root (ans[0])
        """
        for child in self.graph[node]:
            if child != parent:
                self.dfs(child, node)

                # count at subtree = sum of count of children subtrees
                self.count[node] += self.count[child]

                # subans at subtree = subans at child subtree
                # plus 1 for each child node
                # therefore, ans at subtree =
                # sum of ans of children subtrees
                # plus sum of count of nodes in children subtrees
                self.ans[node] += self.ans[child] + self.count[child]
        
    def dfs2(self, node: int, parent: int) -> None:
        """
        Calculate the correct distances at all non-root nodes
        """
        for child in self.graph[node]:
            if child != parent:
                # ans at child = ans at parent
                # minus 1 for each node in child subtree (equal to count of nodes in child subtree)
                # since child subtree has 1 less dist for each of its node
                # plus total number of nodes
                # minus number of nodes at child subtree
                # since child must add 1 extra dist for each node in parent subtree
                self.ans[child] = (self.ans[node] - self.count[child]) + (self.n - self.count[child])
                
                self.dfs2(child, node)
