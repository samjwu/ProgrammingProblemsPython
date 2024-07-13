class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)

        idx = [i for i in range(n)]

        # only keep indices of robos moving right on stack
        # for tracking collisions with robos moving left
        stk = []

        ans = []
        
        idx.sort(key=lambda x: positions[x])

        for curr in idx:
            if directions[curr] == "R":
                stk.append(curr)
            else:
                # if going left, check stack for collision
                while stk and healths[curr] > 0:
                    prev = stk.pop()

                    if healths[prev] > healths[curr]:
                        healths[prev] -= 1
                        healths[curr] = 0
                        stk.append(prev)
                    elif healths[prev] < healths[curr]:
                        healths[prev] = 0
                        healths[curr] -= 1
                    else:
                        healths[prev] = 0
                        healths[curr] = 0

        for i in range(n):
            if healths[i] > 0:
                ans.append(healths[i])

        return ans
