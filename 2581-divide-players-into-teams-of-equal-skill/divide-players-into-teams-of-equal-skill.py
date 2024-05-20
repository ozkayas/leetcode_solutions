class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        teamTarget = sum(skill) // (len(skill)/2)
        freq = defaultdict(int)
        chemSum = 0

        for sk in skill:
            pairOfSk = teamTarget - sk
            if pairOfSk in freq:
                chemSum += (pairOfSk * sk)
                freq[pairOfSk] -= 1
                if freq[pairOfSk] == 0:
                    del freq[pairOfSk]
            else:
                freq[sk] += 1

        return int(chemSum) if len(freq) <= 0 else -1



        