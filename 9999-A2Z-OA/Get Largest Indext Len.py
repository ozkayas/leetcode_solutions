"""
https://www.reddit.com/r/leetcode/comments/1eqh45s/amazon_oa/
"""
# Bu soru russian doll envelope sorusunun neredeyse aynisi. Tum test caseler yok ama bu sekilde yapilabilir.
# https://leetcode.com/problems/russian-doll-envelopes/

def solve(f1, f2):
    pairs = []
    for i in range(len(f1)):
        pairs.append((f1[i], f2[i]))
    pairs.sort(key = lambda x: (x[0], -x[1]))
    print(pairs)
    # We will find LIS of the pairs
    ans = []
    for pair in pairs:
        if not ans or pair[1] > ans[-1]:
            ans.append(pair[1])
        else:
            low = 0
            high = len(ans) - 1
            while low < high:
                mid = low + (high - low) // 2
                if ans[mid] < pair[1]:
                    low = mid + 1
                else:
                    high = mid
            ans[low] = pair[1]


    return len(ans)



print(solve([4, 5, 3, 1, 2], [2, 1, 3, 4, 5])) # 3
print(solve([4, 5, 3, 1, 2, 3], [2, 1, 3, 4, 5, 8])) # 3
