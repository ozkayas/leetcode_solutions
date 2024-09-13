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


from typing import List, Tuple


def KMP_search(pattern: str, text: str) -> Tuple[bool, int, int]:
    # Edge case if pattern is empty
    if not pattern:
        return False, -1, -1

    M = len(pattern)
    N = len(text)

    # Get the LSP array for the pattern
    lsp = getLsp(pattern)

    i = 0  # index for text
    j = 0  # index for pattern

    while i < N:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        # If we found the pattern
        if j == M:
            start = i - j
            end = i - 1
            return True, start, end

        # Mismatch after j matches
        elif i < N and pattern[j] != text[i]:
            # Do not match lsp[0..lsp[j-1]] characters, they will match anyway
            if j != 0:
                j = lsp[j - 1]
            else:
                i += 1

    return False, -1, -1  # Pattern not found


print(getLsp("aaacaaaa"))
print(getLsp("onions"))

print(KMP_search("onions", "onionionsions"))
print(KMP_search("onions", "onionns"))
print(KMP_search("", "onionns"))
