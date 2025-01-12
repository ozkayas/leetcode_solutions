class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        N = len(s)
        if N % 2 != 0: return False

        open_locked, unlocked = 0, 0
        for i in range(N):
            if locked[i] == "0":
                unlocked += 1
            else:
                if s[i] == "(":
                   open_locked += 1
                else:
                    if open_locked > 0:
                        open_locked -= 1
                    elif unlocked > 0:
                        unlocked -= 1
                    else:
                        return False
        # Match remaining open brackets with unlocked characters.
        balance = 0
        for i in range(N - 1, -1, -1):
            if locked[i] == "0":
                balance -= 1
                unlocked -= 1
            elif s[i] == "(":
                balance += 1
                open_locked -= 1
            elif s[i] == ")":
                balance -= 1
            if balance > 0:
                return False
            if unlocked == 0 and open_locked == 0:
                break

        if open_locked > 0:
            return False

        return True

