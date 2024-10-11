class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)

        # store time and index
        # use positive index for joiner, negative index for leaver
        friends = []
        
        for i in range(n):
            # arrival time, index
            friends.append([times[i][0], i])
            # leave time, inverted index
            friends.append([times[i][1], ~i])

        friends.sort()

        # to track open chairs
        openMinHeap = list(range(n))

        # to track taken chairs
        takenMinHeap = []

        for time, friend in friends:
            # calculate leavers
            while takenMinHeap and takenMinHeap[0][0] <= time:
                leaveTime, chair = heapq.heappop(takenMinHeap)
                heapq.heappush(openMinHeap, chair)

            # calculate joiners
            if friend >= 0:
                chair = heapq.heappop(openMinHeap)
                if friend == targetFriend:
                    return chair
                heapq.heappush(takenMinHeap, [times[friend][1], chair])

        return -1
