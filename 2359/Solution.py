class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        ans = -1
        min_dist = float('inf')

        dists1 = [-1] * n
        dists2 = [-1] * n

        self.dfs(node1, 0, edges, dists1)
        self.dfs(node2, 0, edges, dists2)

        for i in range(n):
            # check reachable nodes with minimal distance
            if min(dists1[i], dists2[i]) >= 0 and max(dists1[i], dists2[i]) < min_dist:
                min_dist = max(dists1[i], dists2[i])
                ans = i

        return ans

    def dfs(self, node: int, curr_dist: int, edges: List[int], dists: List[int]) -> None:
        # traverse non-terminal and unvisited nodes
        while node != -1 and dists[node] == -1:
            dists[node] = curr_dist
            curr_dist += 1
            node = edges[node]
