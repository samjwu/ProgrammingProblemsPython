class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = [0] * 26
        for task in tasks:
            freqs[ord(task) - ord('A')] += 1
        
        maxHeap = []
        for freq in freqs:
            if freq > 0:
                maxHeap.append(-freq)
        heapq.heapify(maxHeap)

        time = 0
        while maxHeap:
            cycle = n + 1
            finishedTasks = 0
            remainingTasks = []

            while cycle > 0 and maxHeap:
                cycle -= 1

                finishedTasks += 1

                currFreq = -heapq.heappop(maxHeap)

                if currFreq > 1:
                    remainingTasks.append(-(currFreq - 1))

            for remaining in remainingTasks:
                heapq.heappush(maxHeap, remaining)
            
            # if there are more cycles, add one full cycle of time
            if maxHeap:
                time += n+1
            # otherwise just add time to complete the last tasks
            else:
                time += finishedTasks if not maxHeap else n + 1

        return time
