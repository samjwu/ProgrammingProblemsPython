class RandomizedSet:

    def __init__(self):
        self.numList = []
        self.idxDict = {}

    def insert(self, val: int) -> bool:
        if val not in self.idxDict:
            self.numList.append(val)
            
            self.idxDict[val] = len(self.numList) - 1
            
            return True
        
        return False

    def remove(self, val: int) -> bool:
        if val in self.idxDict:
            idx = self.idxDict[val]
            
            last = self.numList[-1]
            
            self.numList[idx] = last
            
            self.idxDict[last] = idx
            
            self.numList.pop()
            
            self.idxDict.pop(val, 0)
            
            return True
        
        return False

    def getRandom(self) -> int:
        return self.numList[random.randint(0, len(self.numList) - 1)]
