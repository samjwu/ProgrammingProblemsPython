class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(heights)
        m = len(queries)

        ans = [-1] * m

        minHeap = []

        # store (height jumping from, query index)
        simplifiedQueries = [[] for i in heights]

        for queryIndex, query in enumerate(queries):
            a, b = query

            # to simplify, make b the bigger index
            if a > b:
                a, b = b, a

            if heights[a] < heights[b] or a == b:
                # since a < b, solve simple cases by moving a to b
                # or answer is already there with no action
                ans[queryIndex] = b
            else:
                # otherwise heights[a] >= heights[b]
                # and we must do a query to find a jumping point from heights[a]
                simplifiedQueries[b].append((heights[a], queryIndex))

        for currHeightIndex, height in enumerate(heights):
            # if current height is a possible solution for a simple query,
            # take it off the heap (since the simple query was solved)
            # continue for all simple queries where this is possible
            while minHeap and minHeap[0][0] < height:
                queryHeight, queryIndex = heapq.heappop(minHeap)
                ans[queryIndex] = currHeightIndex

            # sets the loop invariant for check above
            # the heap queries will always have starting height index <= current height index
            for simpleQuery in simplifiedQueries[currHeightIndex]:
                heapq.heappush(minHeap, simpleQuery)

        return ans
