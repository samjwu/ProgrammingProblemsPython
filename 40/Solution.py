class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        candidates.sort()

        self.recurse(candidates, target, 0, [], ans)

        return ans

    def recurse(self, candidates: List[int], target: int, idx: int, path: List[int], ans: List[List[int]]) -> None:
        # backtrack
        if target < 0:
            return

        if target == 0:
            ans.append(path)
            return

        for i in range(idx, len(candidates)):
            # skip duplicates
            if i > idx and candidates[i] == candidates[i - 1]:
                continue

            # try taking candidate number
            self.recurse(candidates, target - candidates[i], i + 1, path + [candidates[i]], ans)
