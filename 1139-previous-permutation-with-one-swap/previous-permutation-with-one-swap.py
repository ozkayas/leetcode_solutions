class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        N = len(arr)

        # Returns the idx of the next smaller value, scan from back
        def nextSmallerIndex(arr:list, target:int) -> int:
            i = len(arr)-1
            while arr[i] >= target:
                i -= 1
            nextSmaller = arr[i]
            while arr[i] == nextSmaller:
                i -= 1
            return i + 1


        # Reverse loop and find the num that increases
        prev = arr[-1]
        i = N-1
        while i >= 0 and arr[i] <= prev:
            prev = arr[i]
            i -= 1
        if i == -1: return arr

        # We found the candidate to be swapped: arr[i]
        # Find the next smaller thann arr[i]
        swap_id = nextSmallerIndex(arr, arr[i])
        arr[i], arr[swap_id] = arr[swap_id], arr[i]

        return arr

     
"""
[1,9,4,6,7]
   ^.  -> 9 to be replaced, but with what? -> The next smaller value than 9
[1,7,4,6,9]

[1,5,4,6,7]
[1,4,5,6,7]

"""