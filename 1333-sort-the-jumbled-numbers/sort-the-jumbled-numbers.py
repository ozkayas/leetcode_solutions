class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def convert(n: int, mapping: List[int]) -> int:
            buffer = [str(mapping[int(ch)]) for ch in str(n)]
            return int("".join(buffer))

        # zipp = [(669, 0, 991), (7, 1, 338), (7, 2, 38)]
        zipp = []
        for i, n in enumerate(nums):
            zipp.append( (convert(n, mapping), i, n )  )
    

        return [i[2] for i in sorted(zipp)]


        