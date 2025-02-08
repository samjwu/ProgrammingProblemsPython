class NumberContainers:

    def __init__(self):
        self.num_to_idxset = collections.defaultdict(SortedSet)
        self.idx_to_num = {}

    def change(self, index: int, number: int) -> None:
        # if existing number, remove from set
        if index in self.idx_to_num:
            prev_num = self.idx_to_num[index]

            self.num_to_idxset[prev_num].remove(index)
            if not self.num_to_idxset[prev_num]:
                del self.num_to_idxset[prev_num]

        self.num_to_idxset[number].add(index)
        self.idx_to_num[index] = number

    def find(self, number: int) -> int:
        if number in self.num_to_idxset and self.num_to_idxset[number]:
            return self.num_to_idxset[number][0]

        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
