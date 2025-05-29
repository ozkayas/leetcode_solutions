class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        N, total =len(skill), sum(skill)
        teams = N//2
        if total % teams != 0: return -1

        target = total // teams
        ans = 0
        l, r = 0, N-1
        skill.sort()

        while l < r:
            if skill[l] + skill[r] != target:
                return -1
            else:
                ans += skill[l]*skill[r]
                l += 1
                r -= 1

        return ans


                    

        