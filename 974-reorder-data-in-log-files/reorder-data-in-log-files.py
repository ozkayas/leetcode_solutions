class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def helper(s:str):
            left, right = s.split(" ", 1)
            if right[0].isdigit():
                return (1,)
            else:
                return (0, right, left)



        return sorted(logs, key = helper)
        