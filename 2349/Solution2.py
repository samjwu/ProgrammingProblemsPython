class NumberContainers:

    def __init__(self):
        self.num_to_idx_minheap = collections.defaultdict(list)
        self.idx_to_num = {}

    def change(self, index: int, number: int) -> None:
        heapq.heappush(self.num_to_idx_minheap[number], index)
        self.idx_to_num[index] = number

    def find(self, number: int) -> int:
        if not self.num_to_idx_minheap[number]:
            return -1

        # check min heap for smallest valid index
        while self.num_to_idx_minheap[number]:
            index = self.num_to_idx_minheap[number][0]

            # index is valid
            if self.idx_to_num.get(index) == number:
                return index

            # remove invalid index
            heapq.heappop(self.num_to_idx_minheap[number])

        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
