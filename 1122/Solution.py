class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = Counter(arr1)
        
        ans = []
        
        for key in arr2:
            for i in range(freq[key]):
                ans.append(key)
                
        arr1.sort()
        
        for val in arr1:
            if val not in arr2:
                ans.append(val)
        
        return ans
