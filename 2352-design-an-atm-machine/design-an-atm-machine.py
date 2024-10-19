class ATM:

    def __init__(self):
        self.banknotes = [[0, 20], [0, 50], [0, 100], [0, 200], [0, 500]]
        

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.banknotes[i][0] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        temp = [0] * 5
        for i in reversed(range(5)):
            if amount <= 0:
                break
            if self.banknotes[i][1] <= amount:
                needed = amount // self.banknotes[i][1]
                to_use = min(needed, self.banknotes[i][0])
                temp[i] = to_use
                amount -= to_use * self.banknotes[i][1]

        if amount != 0:
            return [-1]
        else:
            for i in range(5):
                self.banknotes[i][0] -= temp[i]
            return temp



        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)