'''
Amazon's database doesn’t support very large numbers, so numbers are stored as a string of binary characters, '0' and '1'. Accidentally, a '!' was entered at some positions and it is unknown whether they should be '0' or '1'.
The string of incorrect data is made up of the characters '0', '1' and '!' where '!' is the character that got entered incorrectly. '!' can be replaced with either '0' or '1'. Due to some internal faults, some errors are generated every time '0' and '1' occur together as '01' or '10' in any subsequence of the string. It is observed that the number of errors a subsequence '01' generates is x, while a subsequence '10' generates y errors.
Determine the minimum total errors generated. Since the answer can be very large, return it modulo 109+7.
Note: A subsequence of a string is obtained by omitting zero or more characters from the original string without changing their order.
Hint: It can be proved that (a + b) % c = ((a% c) + (b % c)) % c where a, b, and c are integers and % represents the modulo operation.

Function Description

Complete the function getMinErrors in the editor.

getMinErrors has the following parameter(s):

String errorString: a string of characters '0', '1', and '!'
int x: the number of errors generated for every occurrence of subsequence 01
int y: the number of errors generated for every occurrence of subsequence 10
Returns

int: the minimum number of errors possible, modulo 109+7

Example 1:

Input:  errorString = "101!1", x = 2, y = 3
Output: 9 
Explanation:

If the '!' at index 3 is replaced with '0', the string is "10101". The number of times the subsequence 01 occurs is 3 at indices (1, 2), (1, 4), and (3, 4). The number of times the subsequence 10 occurs is also 3, indices (0, 1), (0, 3) and (2, 3). The number of errors is 3 * x + 3 * y = 6 + 9 = 15.
   
If the '!' is replaced with '1', the string is "10111". The subsequence 01 occurs 3 times and 10 occurs 1 time. The number of errors is 3 * x + y = 9.
      
The minimum number of errors is min(9, 15) modulo (109 + 7) = 9.  
      
Example 2:

Input:  errorString = "01!0", x = 2, y = 2
Output: 8 
Explanation:

The better string is 0100 with one substring 01 and two substrings 10 making total errors generate = 21 + 32 = 8 (p.s. 2 + 1 + 3 + 2 = 8 makes more sense to me... Many thanks inadvance if you could help clarify the calculation here 🤝)
      
Example 3:

Input:  errorString = "!!!!!!!", x = 23, y = 27
Output: 0 
Explanation:

There is a tie for the best string generated, 00000 or 11111, with zero substrings 01 or 10.
      
Constraints:
1<= len (errorString)<=105
0 <= x, y <= 105
s consists only of characters '0', '1', and 'l'


'''
import sys
from typing import List

MOD = 10 ** 9 + 7

class MinimumTotalErrors:

    def solve(self, s: str, x: int, y: int) -> int:
        n = len(s)
        if n == 0:
            return 0

        # Initialize dp array with large values
        dp = [[sys.maxsize] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            if s[i - 1] == '0' or s[i - 1] == '!':
                for j in range(i + 1):
                    if dp[i - 1][j] < sys.maxsize:
                        dp[i][j] = min(dp[i][j], dp[i - 1][j] + j * y)

            if s[i - 1] == '1' or s[i - 1] == '!':
                for j in range(1, i + 1):
                    if dp[i - 1][j - 1] < sys.maxsize:
                        dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + x * (i - j))

        # Find the minimum value in the last row of the dp array
        return min(dp[n])


solver = MinimumTotalErrors()

# print(solver.solve("101!1", 2, 3))  # Expected Output: 9
# print(solver.solve("01!0", 2, 2))  # Expected Output: 9
# print(solver.solve("!!!!!", 23, 27))  # Expected Output: 9
print(solver.solve("10!!01!", 2 , 3))  # Expected Output: 9
print(solver.solve("1000010", 2 , 3))  # Expected Output: 9
print(solver.solve("1000011", 2 , 3))  # Expected Output: 9
print(solver.solve("1001011", 2 , 3))  # Expected Output: 9
print(solver.solve("1011011", 2 , 3))  # Expected Output: 9


MOD = 10 ** 9 + 7
MOD = 10 ** 9 + 7
MOD = 10 ** 9 + 7


def count_base_errors(errorString, x, y):
    """Temel hata maliyetini hesapla."""
    n = len(errorString)
    base_errors = 0

    # Önceki 0 ve 1 sayısını takip et
    zero_count = 0
    one_count = 0

    # Diziyi tarayarak 01 ve 10 dizilerini say
    for ch in errorString:
        if ch == '0':
            base_errors = (base_errors + one_count * y) % MOD
            zero_count += 1
        elif ch == '1':
            base_errors = (base_errors + zero_count * x) % MOD
            one_count += 1

    return base_errors


def getMinErrors(errorString, x, y):
    n = len(errorString)

    # Temel hata maliyetini hesapla
    base_errors = count_base_errors(errorString, x, y)

    # Soldan sağa ve sağdan sola 0'ların ve 1'lerin sayısını takip et
    pre_zero_count = [0] * n
    pre_one_count = [0] * n
    suf_zero_count = [0] * n
    suf_one_count = [0] * n

    # Soldan sağa: Her pozisyondaki 0 ve 1 sayısını bul
    zeros_count = 0
    ones_count = 0
    for i in range(n):
        if errorString[i] == '0':
            zeros_count += 1
        elif errorString[i] == '1':
            ones_count += 1
        pre_zero_count[i] = zeros_count
        pre_one_count[i] = ones_count

    # Sağdan sola: Her pozisyondaki 0 ve 1 sayısını bul
    zeros_count = 0
    ones_count = 0
    for i in range(n - 1, -1, -1):
        if errorString[i] == '0':
            zeros_count += 1
        elif errorString[i] == '1':
            ones_count += 1
        suf_zero_count[i] = zeros_count
        suf_one_count[i] = ones_count

    # Hataları hesaplama
    min_errors = float('inf')

    # Dizi üzerinde gezerek her ! karakterinin etkisini hesapla
    for i in range(n):
        if errorString[i] == '!':
            # ! karakterini 1 yapma durumu
            errors_01 = pre_zero_count[i] * x  # Önceki 0'ların bu ! ile 01 oluşturması
            errors_10 = suf_zero_count[i] * y  # Sonraki 0'ların bu ! ile 10 oluşturması
            total_errors_1 = (errors_01 + errors_10) % MOD

            # ! karakterini 0 yapma durumu
            errors_10 = pre_one_count[i] * y  # Önceki 1'lerin bu ! ile 10 oluşturması
            errors_01 = suf_one_count[i] * x  # Sonraki 1'lerin bu ! ile 01 oluşturması
            total_errors_0 = (errors_01 + errors_10) % MOD

            # Minimum hatayı bul
            min_errors = min(min_errors, total_errors_1, total_errors_0)

            # Prefix ve suffix tablolardaki güncellemeleri hesapla
            if total_errors_1 < min_errors:
                # ! karakterini 1 yaptığımızda, prefix ve suffix tablolarını güncelle
                for j in range(i + 1, n):
                    if errorString[j] == '0':
                        suf_zero_count[j] -= 1
                    elif errorString[j] == '1':
                        suf_one_count[j] -= 1
            elif total_errors_0 < min_errors:
                # ! karakterini 0 yaptığımızda, prefix ve suffix tablolarını güncelle
                for j in range(i + 1, n):
                    if errorString[j] == '0':
                        suf_zero_count[j] += 1
                    elif errorString[j] == '1':
                        suf_one_count[j] += 1

    # Temel hata maliyetini ve minimum hata maliyetini ekleyerek sonucu döndür
    return (base_errors + min_errors) % MOD


# Örnek kullanım
errorString = "101!1"
x = 2
y = 3
print(getMinErrors("10!!0!1!", 2, 3))  # Çıktı: 9



