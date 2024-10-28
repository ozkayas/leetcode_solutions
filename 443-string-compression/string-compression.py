class Solution:
    def compress(self, chars: List[str]) -> int:
        w = r = 0
        while r < len(chars):
            curCh = chars[r]
            count = 0
            while r < len(chars) and chars[r] == curCh:
                count += 1
                r += 1
            
            chars[w] = curCh
            w += 1
             
            if count > 1:
                for c in str(count):
                    chars[w] = c
                    w += 1

        return w
            

        