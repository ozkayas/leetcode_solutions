main() {
  Solution().moveZeroes([0, 1, 0, 3, 12]);
}

class Solution {
  void moveZeroes(List<int> nums) {
    int reader = 0;
    int writer = 0;

    while (reader < nums.length) {
      if (nums[reader] != 0) {
        nums[writer] = nums[reader];
        writer++;
      }
      reader++;
    }
    while (writer < nums.length) {
      nums[writer] = 0;
      writer++;
    }
  }
}
