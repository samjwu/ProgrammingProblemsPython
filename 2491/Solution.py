class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        
        n = len(skill)
        
        ans = 0

        teamSkill = skill[0] + skill[n-1]

        for i in range(n//2):
            if skill[i] + skill[n-1-i] != teamSkill:
                return -1

            ans += skill[i] * skill[n-1-i]

        return ans
