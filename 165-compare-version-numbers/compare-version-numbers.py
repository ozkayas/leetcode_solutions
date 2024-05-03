class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ans = 0

        v1 = [int(i) for i in version1.split(".")]
        v2 = [int(i) for i in version2.split(".")]

        maxLen = max( len(v1), len(v2) )

        for i in range(maxLen):
            num1 = int(v1[i]) if i < len(v1) else 0
            num2 = int(v2[i]) if i < len(v2) else 0

            if num1 > num2:
                return 1
            if num2 > num1:
                return -1

        return ans
          
        
        