class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)

        # calc in-degree
        in_degree = [0] * n
        for person in range(n):
            in_degree[favorite[person]] += 1

        # queue up all nodes with zero in-degree
        q = deque()
        for person in range(n):
            if in_degree[person] == 0:
                q.append(person)
        
        # track depth of non cycle nodes (chain)
        # since the chain may be connected by a 2-node cycle
        depth = [1] * n

        # remove non cycle nodes with topological sort
        while q:
            current_node = q.popleft()
            next_node = favorite[current_node]

            depth[next_node] = max(depth[next_node], depth[current_node] + 1)

            in_degree[next_node] -= 1
            if in_degree[next_node] == 0:
                q.append(next_node)

        # answer is the max of the longest single cycle
        # or length of cycles between two nodes
        longest_cycle_len = 0
        two_node_cycles_len = 0

        # detect cycles
        for person in range(n):
            if in_degree[person] == 0:
                continue

            cycle_length = 0
            current = person

            while in_degree[current] != 0:
                in_degree[current] = 0
                cycle_length += 1
                current = favorite[current]

            if cycle_length == 2:
                # for 2 node cycles, add the depth of both nodes
                # since a chain may be involved (from topological sort)
                two_node_cycles_len += depth[person] + depth[favorite[person]]
            else:
                longest_cycle_len = max(longest_cycle_len, cycle_length)

        return max(longest_cycle_len, two_node_cycles_len)
