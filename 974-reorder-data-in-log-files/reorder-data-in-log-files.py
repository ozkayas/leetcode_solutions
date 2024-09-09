class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:


        def compare(s: str) -> tuple:
            [id, con] = s.split(" ", 1)
            if con[0].isdigit():
                return (1, )
            else:
                return (0, con, id)

        logs.sort(key = compare)
        return logs
        