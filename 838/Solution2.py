class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        forces = [0] * n

        # calculate R forces
        force = 0

        for i in range(n):
            if dominoes[i] == 'R':
                force = n
            elif dominoes[i] == 'L':
                force = 0
            else:
                force = max(force-1, 0)

            forces[i] += force

        # calculate L forces
        force = 0

        for i in range(n-1, -1, -1):
            if dominoes[i] == 'L':
                force = n
            elif dominoes[i] == 'R':
                force = 0
            else:
                force = max(force-1, 0)

            forces[i] -= force

        # calculate direction based on force sums
        ans = []
        for force in forces:
            if force == 0:
                ans.append('.')
            elif force > 0:
                ans.append('R')
            else: # force < 0
                ans.append('L')
        return "".join(ans)
