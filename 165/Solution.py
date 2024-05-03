class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = version1.split(".")
        ver2 = version2.split(".")
        
        m = len(ver1)
        n = len(ver2)
        
        short = min(m, n)
        long = max(m, n)
        
        for i in range(short):
            if int(ver1[i]) > int(ver2[i]):
                return 1
            elif int(ver1[i]) < int(ver2[i]):
                return -1
            
        v1Has = False
        v2Has = False
        
        if m > n:
            v1Has = self.hasNonzero(ver1, short)
        elif m < n:
            v2Has = self.hasNonzero(ver2, short)
        
        if v1Has:
            return 1
        elif v2Has:
            return -1
        
        return 0
    
    def hasNonzero(self, ver: list[str], short: int) -> bool:
        n = len(ver)
        
        for i in range(short, n):
            if int(ver[i]) > 0:
                return True
            
        return False
