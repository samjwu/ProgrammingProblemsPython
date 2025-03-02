class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        id_map = {}

        for id, val in nums1:
            if id in id_map:
                id_map[id] += val
            else:
                id_map[id] = val

        for id, val in nums2:
            if id in id_map:
                id_map[id] += val
            else:
                id_map[id] = val

        ans = [[id, val] for id, val in sorted(id_map.items())]

        return ans
