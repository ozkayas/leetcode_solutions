
main() {
  var result = Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]);
  print(result);
}

class Solution {
  /// Using a two pointer approach, head for holding resulting array, end for shifting till the end.
  int removeDuplicates(List<int> nums) {
    int head = 0; // pointer
    int end = 0;

    while (end < nums.length) {
      if (nums[end] > nums[head]) {
        head++;
        nums[head] = nums[end];
      }
      end++;
    }

    return head + 1; // return not pointing index, number of elements
  }
}
