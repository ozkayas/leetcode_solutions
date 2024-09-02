"""
Amazon recently conducted interviews where the candidates were asked to sort the permutation p of length n. The ith candidate sorted the permutation in moves[i] moves. To verify the results once more, the interviewers want to find if it is possible to sort the permutation in the given number of moves. Given the original permutation array p and the number of moves made by each of the q candidates, find whether you can sort the permutation p by performing exactly moves[i] moves. In one move you can swap values at any two distinct indices. Return the answer as a binary string of length q. The value at the ith index should be 1 if it is possible to sort the permutation p in exactly moves[i] moves, or 0 otherwise.
Note: A permutation is a sequence of n distinct integers such that each integer between [1, n] appears exactly once. For example, [1,3,2,4] is a permutation of size 4, but [1,3,4,5] or [1,2,2,4] are not.
Function Description
Complete the function sortPermutation in the editor.
sortPermutation has the following parameters:
1. int[] p: the original permutation array
2. int[] moves: the number of moves made by each candidate
Returns
String: a binary string of length q where each character is either '1' or '0'

Example 1:

Input:  p = [2, 3, 1, 4], moves = [2, 3]
Output: "10"
Explanation:
      - In the first query, moves[0] = 2, We can sort the given permutation in exactly 2 moves,

Swap 0th and 2nd index, p = [1,3,2,4]
Swap 1st and 2nd index, p = [1,2,3,4]

      - In the second query, moves[1] = 3, It can be shown that It is not possible to sort the given permutation in exactly 3 moves.

The answer is the string "10".
"""
from typing import List


class Solution():
    ############ BU SORU TAM NET degil ama hackerrankteki benzer sorunun cozumunu ekliyorum, swap yaparak sorting mekanizmasi, minimum swap heaplama
    ### Min swap hesaplarken cycle- detection yapiyor, yerinde olmayan bir numaradan baslayip zincirleme kim kimin yerinde diye ilkine donene kadar cycle ariyor.
    """
    def minimumSwaps(arr):

    # Helper getters
    def isInPlace(i: int) -> int:
        return i+1 == arr[i]

    def trueIdxOf(n) -> int:
        return n - 1

    swaps = 0
    # placed = 0
    # for i in range(len(arr)):
    #     if isInPlace(i):
    #         placed += 1
    # max_swaps_can_be_done = len(arr) - placed -1

    # Detect cycles to calculate min swaps
    visited = set()
    for i in range(len(arr)):
        if arr[i] in visited or isInPlace(i):
            continue

        # Start a cycle detection with this as cur
        cycle_size = 0
        cur = arr[i]
        visited.add(cur)

        # curin olmasi gerektigi yerdeki numara cycle da yoksa. Onu da cycle a ekle
        # o degerden devam et cycle taramaya
        while arr[trueIdxOf(cur)] not in visited:
            cur = arr[trueIdxOf(cur)]
            visited.add(cur)
            cycle_size += 1

        swaps += cycle_size

    return swap
    """

    def sortPermutations(self, p: List[int], moves: List[int]):
        pass
        # Ustteki aciklamayi oku, belki minswap ve max swap kullanarak cozulebilir.
