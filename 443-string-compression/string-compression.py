class Solution:
    def compress(self, chars: List[str]) -> int:
        w = r= 0

        while r < len(chars):
            count = 0
            curChar = chars[r]
            while r < len(chars) and chars[r] == curChar:
                count += 1
                r += 1
            chars[w] = curChar
            w += 1

            if count > 1:
                for digit in str(count):
                    chars[w] = digit
                    w += 1
            
        
        return w