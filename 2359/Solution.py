from typing import List

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        """
        Find a node that can be reached from node1 and node2
        And is also closest to both of them,
        such that the max distance from either one is minimized
        """
        n = len(edges)
        closest_node = -1
        min_dist = float('inf')

        dists1 = [-1] * n
        dists2 = [-1] * n

        self.compute_dists(node1, 0, edges, dists1)
        self.compute_dists(node2, 0, edges, dists2)

        for i in range(n):
            # check reachable nodes with minimal distance
            if min(dists1[i], dists2[i]) >= 0 and max(dists1[i], dists2[i]) < min_dist:
                min_dist = max(dists1[i], dists2[i])
                closest_node = i

        return closest_node

    def compute_dists(self, node: int, curr_dist: int, edges: List[int], dists: List[int]) -> None:
        """
        Traverse non-terminal and unvisited nodes
        Compute their distance from the parent
        """
        while node != -1 and dists[node] == -1:
            dists[node] = curr_dist
            curr_dist += 1
            node = edges[node]
