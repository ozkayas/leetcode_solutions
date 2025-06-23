'''https://www.fastprep.io/problems/amazon-minimize-variation


As an operations engineer at Amazon, you are responsible for organizing the distribution of n different items in the warehouse. The size of each product is provided in an array productSize, where productSize[i] represents the size of the ith product.

You construct a new array called variation, where each element variation[i] is the difference between the largest and smallest product sizes among the first i products. Mathematically, this is defined as:

variation[i] = max(productSize[1], productSize[2], ..., productSize[i]) - min(productSize[1], productSize[2], ..., productSize[i])

Your goal is to arrange the products in a way that minimizes the total variation, i.e., the sum of variation[1] + variation[2] + ... + variation[n]. Determine the minimum possible value of this sum after you have reordered the products.

Function Description

Complete the function minimizeVariation in the editor.

My deepest thanks to the incredible friend who helped bring the problems to completion. 🐳

Example 1:

Input: productSize = [3, 1, 2]
Output: 3
Explanation:

  
By reordering the products as productSize = [2,3,1]:
        

          
variation[0] = max(2) - min(2) = 2-2 = 0.

          
variation[1] = max(2,3) - min(2,3) = 3-2 = 1.

          
variation[2] = max(2,3,1) - min(2,3,1) = 3-1 = 2.

        

The sum is variation[0] + variation[1] + variation[2] = 0+1+2 = 3. This is the minimum possible total variation after rearranging.
      
      
Example 2:

Input: productSize = [6, 1, 4, 2]
Output: 9
Explanation:

  
By reordering the products as productSize = [1,2,4,6]:
        

          
variation[0] = max(1) - min(1) = 1-1 = 0.

          
variation[1] = max(1,2) - min(1,2) = 2-1 = 1.

          
variation[2] = max(1,2,4) - min(1,2,4) = 4-1 = 3.

          
variation[3] = max(1,2,4,6) - min(1,2,4,6) = 6-1 = 5.

        

The minimum total variation is variation[0] + variation[1] + variation[2] + variation[3] = 0+1+3+5 = 9
'''
def minimizeVariation(productSize):
    n = len(productSize)
    productSize.sort()
    # Komşular arası en küçük farkın başladığı window'u bul
    min_idx = min(range(n-1), key=lambda i: productSize[i+1] - productSize[i])
    left = min_idx
    right = min_idx+1
    result = [productSize[left], productSize[right]]
    while left > 0 or right < n-1:
        if left == 0:
            right += 1
            result.append(productSize[right])
        elif right == n-1:
            left -= 1
            result.append(productSize[left])
        else:
            if (productSize[left] - productSize[left-1]) <= (productSize[right+1] - productSize[right]):
                left -= 1
                result.append(productSize[left])
            else:
                right += 1
                result.append(productSize[right])
    total = 0
    cur_min = cur_max = None
    for i in range(n):
        sub = result[:i+1]
        cur_min = min(sub)
        cur_max = max(sub)
        total += cur_max - cur_min
    print(f"Final order: {result}, Total variation: {total}")
    return total






## TEST CASES, assertions
if __name__ == "__main__":
    assert minimizeVariation([3, 1, 2]) == 3, "Test Case 1 Failed"
    assert minimizeVariation([6, 1, 4, 2]) == 9, "Test Case 2 Failed"
    assert minimizeVariation([5, 3, 8, 2]) == 10, "Test Case 3 Failed"
    assert minimizeVariation([1,2,3,9,5,5,5]) == 17, "Test Case 4 Failed"
    print("\n 😎 All test cases passed!\n")  # If no assertion error, this will print