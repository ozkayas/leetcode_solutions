class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        # ["c","f","j"], target = "c"
        #.  f   t   t  
        # search for > target values

        # Edge case, last letter is not greater than target
        if letters[-1] <= target:
            return letters[0]


        l, r = 0, len(letters) -1
        ans = ""

        while l <= r:

            m = l + (r-l)//2

            if target < letters[m]:
                ans = letters[m]
                r = m - 1
            else:
                l = m + 1

        return ans

        