class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:


        def order(log:str):
            (tip, data) = log.split(" ", 1)
            if data[0].isalpha(): # if letter type
                return (0, data, tip)
            else:
                return (1, None)
            

        return sorted(logs, key=order)
        