class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        N = len(arr)
        targetIndex = bisect_left(arr, x)

        l, r = targetIndex-1, targetIndex
        ans = []

        while len(ans) < k:
            if l >= 0 and r < N:
                leftDif = abs(arr[l] - x)
                rightDif = abs(arr[r] - x)
                if leftDif <= rightDif:
                    ans.append(arr[l])
                    l -= 1
                else:
                    ans.append(arr[r])
                    r += 1
            elif r < N:
                ans.append(arr[r])
                r += 1
            else:
                ans.append(arr[l])
                l -= 1
        
        return sorted(ans)




        