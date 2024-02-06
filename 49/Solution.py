class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        
        baseWordToAnagrams = defaultdict(list)
        
        for s in strs:
            baseWord = "".join(sorted(s))
            
            baseWordToAnagrams[baseWord].append(s)
            
        for baseWord in baseWordToAnagrams:
            ans.append(baseWordToAnagrams[baseWord])
        
        return ans
