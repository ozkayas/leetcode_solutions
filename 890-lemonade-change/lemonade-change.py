class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # Holds moneys at repo
        self.repo = defaultdict(int)

        def canChange(bill: int) -> bool:
            if bill == 10:
                if self.repo[5]:
                    self.repo[5] -= 1
                    return True
                else:
                    return False
            elif bill == 20:
                if self.repo[5] and self.repo[10]:
                    self.repo[5] -= 1
                    self.repo[10] -= 1
                    return True
                elif self.repo[5] > 2:
                    self.repo[5] -= 3
                    return True
                else:
                    return False

        for bill in bills:
            if bill == 5:
                self.repo[5] += 1
            elif bill == 10 and canChange(bill):
                self.repo[10] += 1
            elif bill == 20 and canChange(bill):
                self.repo[20] += 1
            else:
                return False

        return True