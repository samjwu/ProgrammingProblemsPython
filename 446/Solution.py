class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        
        ans = 0
        
        # freqs[end index][delta] = count of subseqs
        # up to nums[end index] with difference of delta
        # note freqs allows for 2 element subseqs
        freqs = [defaultdict(int) for i in range(n)]
        
        for i in range(n):
            for j in range(i):
                delta = nums[i] - nums[j]
                
                # count of existing subseqs
                # up to index j with difference of delta
                existingSubseqs = 0
                if delta in freqs[j]:
                    existingSubseqs = freqs[j][delta]
                
                # all possible subseqs ending at i =
                # original count of subseqs up to index i with difference of delta
                # + count of existing subseqs ending at j
                # (formed by adding nums[i] to each existing subseq)
                # + 1 new subseq
                # (formed by making the pair nums[j] and nums[i])
                freqs[i][delta] += existingSubseqs + 1
                
                # only add subseqs with >= 3 elements to answer
                ans += existingSubseqs
        
        return ans
