class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)

        if n % groupSize != 0:
            return False

        freq = Counter(hand)

        minHeap = list(freq.keys())
        heapq.heapify(minHeap)

        while minHeap:
            curr = minHeap[0]
            
            for i in range(groupSize):
                # cannot make a straight
                if freq[curr + i] == 0:
                    return False

                freq[curr + i] -= 1

                # last card made a break in future straights
                if freq[curr + i] == 0:
                    if curr + i != heapq.heappop(minHeap):
                        return False

        return True
