class Solution:
    ## Helper method will return the prefix group length
    ## [a, a, a, b,b] => (a,3) , 
    def groupLen(self, chars: List[str]) -> tuple:
        first = chars[0]
        for i in range(len(chars)):
            if chars[i] != first:
                return (first, i)
        return (first, len(chars))

    def compress(self, chars: List[str]) -> int:
        w,r  = -1, 0
        while r < len(chars):
            ch, n = self.groupLen(chars[r:])
            ## do stuff
            w += 1
            chars[w] = ch
            if n > 1:
                for i in range(len(str(n))):
                    w += 1
                    chars[w] = str(n)[i]
            r += n
             
        return w + 1

        