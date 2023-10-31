class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = [pref[0]]
        prev = pref[0]
        
        for i in range(1, len(pref)):
            nex = prev ^ pref[i]
            ans.append(nex)
            prev = pref[i]
            
        return ans
