class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
             return False

        digit = 0
        reversed = 0
        original = x

        while original > 0:
            digit = original % 10
            original = original // 10
            reversed = reversed * 10 + digit

        return reversed == x