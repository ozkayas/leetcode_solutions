

from typing import List


def compress(chars: List[str]) -> int:

    if len(chars) == 1:
        return 1

    i, j = 0,0
    while j < len(chars):   
        while j < len(chars) and chars[j] == chars[i]:
            j += 1
        print(i , j)
        count = j - i
        i += 1
        if count > 1:
            strCount = str(count)
            for c in strCount:
                # i += 1
                chars[i] = c
                i += 1

        print(chars)
    return i









# chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
chars = ["a","a","b","b","c","c","c"]
compress(chars)


