main() {
  Solution().sortedSquares([-7, -3, 2, 3, 11]);
}

class Solution {
  List<int> sortedSquares(List<int> nums) {
    List<int> squaredList = List.filled(nums.length, 0);
    int headPointer = 0;
    int endPointer = nums.length - 1;

    int currentIndex = nums.length - 1;
    while (headPointer <= endPointer) {
      if (nums[headPointer] * nums[headPointer] > nums[endPointer] * nums[endPointer]) {
        squaredList[currentIndex] = nums[headPointer] * nums[headPointer];
        headPointer++;
      } else {
        squaredList[currentIndex] = nums[endPointer] * nums[endPointer];
        endPointer--;
      }
      currentIndex--;
    }

    return squaredList;
  }
}
