class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def minute(event:List[str]) -> List[int]:
            start, end = event[0], event[1]
            sh, sm = start.split(":", 1)
            sh = int(sh)
            sm = int(sm)
            eh, em = end.split(":", 1)
            eh = int(eh)
            em = int(em)
            return [sm + sh*60, em + eh*60]
        
        e1 = minute(event1)
        e2 = minute(event2)

        if e1[0] <= e2[0] <= e1[1] or e2[0] <= e1[0] <= e2[1]:
            return True
        return False


        