class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        m = len(items)
        n = len(queries)
        ans = [0 for i in range(n)]

        items.sort(key=lambda x: x[0])
        # map query value to index in queries
        queryMap = [[queries[i], i] for i in range(n)]
        queryMap.sort(key=lambda x: x[0])

        itemIndex = 0
        best = 0

        for i in range(n):
            query = queryMap[i][0]
            queryIndex = queryMap[i][1]

            while itemIndex < m and items[itemIndex][0] <= query:
                best = max(best, items[itemIndex][1])
                itemIndex += 1

            ans[queryIndex] = best

        return ans
