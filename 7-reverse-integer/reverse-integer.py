class Solution:
    def reverse(self, x: int) -> int:

        digits = deque()
        num = abs(x)
        while num:
            n = num % 10
            digits.append(n)
            num //= 10
        # print(digits)
        

        # build back
        num = 0
        while digits:
            d = digits.popleft()
            num *= 10
            num += d
            if num > (2**31 - 1): return 0

        return num if x >= 0 else -num


        