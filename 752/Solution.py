class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        nextMap = {
            "0": "1",
            "1": "2",
            "2": "3",
            "3": "4",
            "4": "5",
            "5": "6",
            "6": "7",
            "7": "8",
            "8": "9",
            "9": "0",
        }
        
        prevMap = {
            "0": "9",
            "1": "0",
            "2": "1",
            "3": "2",
            "4": "3",
            "5": "4",
            "6": "5",
            "7": "6",
            "8": "7",
            "9": "8",
        }

        q = deque()
        
        seen = set(deadends)        

        turns = 0

        # edge case: starting state is visited
        if "0000" in seen:
            return -1

        q.append("0000")

        seen.add("0000")

        while q:
            n = len(q)

            for i in range(n):
                curr = q.popleft()

                if curr == target:
                    return turns

                for slot in range(4):
                    # try turning each slot to next value
                    newCombination = list(curr)
                    newCombination[slot] = nextMap[newCombination[slot]]
                    newCombination_str = "".join(newCombination)
                    
                    if newCombination_str not in seen:
                        q.append(newCombination_str)
                        seen.add(newCombination_str)

                    # try turning each slot to prev value
                    newCombination = list(curr)
                    newCombination[slot] = prevMap[newCombination[slot]]
                    newCombination_str = "".join(newCombination)
                    
                    if newCombination_str not in seen:
                        q.append(newCombination_str)
                        seen.add(newCombination_str)

            turns += 1

        return -1
