class Solution:
    def maxLength(self, arr: List[str]) -> int:
        memo = [set()]
        
        for string in arr:
            # skip nonunique strings
            if len(set(string)) < len(string):
                continue
                
            subseq1 = set(string)
            
            # create a copy of memo to iterate over
            temp = memo[:]
            
            # try all concatenations
            for subseq2 in temp:
                # skip concatenation that results in nonunique string
                if subseq1 & subseq2:
                    continue
                    
                memo.append(subseq1 | subseq2)
                
        return max(len(subseq) for subseq in memo)
