class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        zip = sorted([(heights[i], names[i]) for i in range(len(names))], reverse = True)

        return [name for h,name in zip]
        