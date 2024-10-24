class Solution:
    def compress(self, chars: List[str]) -> int:
        w = r = 0
        cur_char = chars[0]
        count = 0

        while r < len(chars):
            while r < len(chars) and chars[r] == cur_char:
                count += 1
                r += 1
            
            chars[w] = cur_char
            w += 1

            if count > 1:
                for digit in str(count):
                    chars[w] = digit
                    w += 1

            if r < len(chars):
                cur_char = chars[r]
                count = 0

        return w