class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        sm = sum(skill)
        N = len(skill)
        nOfTeams = N/2
        teamSkill = sm / nOfTeams
        if sm % nOfTeams != 0: return -1

        ans = 0
        skill.sort()
        l, r = 0, N-1

        while l < r:
            sm = skill[l] + skill[r]
            if sm != teamSkill: return -1
            ans += skill[l] * skill[r]
        
            l += 1
            r -= 1
        
        return ans

        