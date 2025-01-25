class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)

        num_idx_pairs = []
        for i in range(n):
            num_idx_pairs.append((nums[i], i))
        num_idx_pairs.sort(key=lambda x: x[0])

        groups = [[num_idx_pairs[0]]]
        for i in range(1, n):
            if num_idx_pairs[i][0] - num_idx_pairs[i-1][0] <= limit:
                groups[-1].append(num_idx_pairs[i])
            else:
                groups.append([num_idx_pairs[i]])

        for group in groups:
            indices = []
            for num, idx in group:
                indices.append(idx)
            indices.sort()

            for i in range(len(indices)):
                nums[indices[i]] = group[i][0]

        return nums
