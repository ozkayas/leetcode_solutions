# Function to count pairs whose sum is divisible by 'K'
def countKdivPairs(A,  K: int):
    # Create a frequency array to count occurrences of all remainders when divided by K
    n = len(A)
    freq = [0] * K

    # Count occurrences of all remainders
    for i in range(n):
        freq[(A[i] % K)] += 1

    # If both pairs are divisible by 'K'
    sum = freq[0] * (freq[0] - 1) / 2

    # count for all i and (k-i) freq pairs
    i = 1
    while i <= K // 2 and i != (K - i):
        sum += freq[i] * freq[K - i]
        i += 1

    # If K is even
    if K % 2 == 0:
        sum += (freq[K // 2] * (freq[K // 2] - 1) / 2)

    return int(sum)


print(countKdivPairs([2,2,1,7,5,3], 4))
print(countKdivPairs([31, 25, 85, 29, 35], 60))
