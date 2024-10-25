class Solution:
    def compress(self, chars: List[str]) -> int:
        w, r = 0, 0
        counter = 0

        while r < len(chars):
            cur_ch = chars[r]

            while r < len(chars) and chars[r] == cur_ch:
                counter += 1
                r += 1
            chars[w] = cur_ch
            w += 1
            if counter > 1:
                for digit in str(counter):
                    chars[w] = digit
                    w += 1
            counter = 0
        return w 