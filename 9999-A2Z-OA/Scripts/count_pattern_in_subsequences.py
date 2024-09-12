## counts 01 in a string. how many times 01 appears in a string
def countPatternInSubsequences(s: str) -> int:
    count0 = 0   # To count '0's found so far
    count01 = 0  # To count "01" subsequences

    for char in s:
        if char == '0':
            count0 += 1  # A new '0' can be the start of a new "01"
        elif char == '1':
            count01 += count0  # Every '0' before this '1' can form a valid "01"

    return count01

# Example usage:
s = "0101"
print(countPatternInSubsequences(s))  # Output: 3
