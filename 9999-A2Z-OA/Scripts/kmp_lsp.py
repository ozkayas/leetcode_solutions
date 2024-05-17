# Code that pre-process the pattern searched and returns the lsp.
# We use lsp array in KMP Algo to search a string, that runs in O(n + m)

from typing import List


def getLsp(pattern:str) -> List[int]:
    M = len(pattern)
    ln, i = 0, 1
    lsp = [0 for _ in range(M)]

    while i < M:
        if pattern[i] == pattern[ln]:
            lsp[i] = ln + 1
            ln += 1
            i += 1

        else:
            if ln != 0:
                ln = lsp[ln-1]
            else:
                lsp[i] = 0
                i += 1
    return lsp

print(getLsp("aaacaaaa"))
print(getLsp("onions"))