class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # determine effect of adding passing student to class pass ratio
        def calculatePassRatioDelta(passes: int, total: int):
            return (passes + 1) / (total + 1) - passes / total

        # store (delta, passes, total students)
        maxHeap = []

        for passes, total in classes:
            delta = calculatePassRatioDelta(passes, total)
            heapq.heappush(maxHeap, (-delta, passes, total))

        for i in range(extraStudents):
            # get class with best delta
            delta, passes, total = heapq.heappop(maxHeap)

            heapq.heappush(maxHeap,
                (
                    -calculatePassRatioDelta(passes + 1, total + 1),
                    passes + 1,
                    total + 1,
                ),
            )

        finalRatio = 0

        while maxHeap:
            delta, passes, total = heapq.heappop(maxHeap)
            finalRatio += passes / total

        return finalRatio / len(classes)
