main() {
  Solution().removeElement([3, 2, 2, 3], 3);
}

class Solution {
  int removeElement(List<int> nums, int val) {
    if (nums.isEmpty) return 0;
    int reader = 0;
    int writer = 0;

    while (reader < nums.length) {
      if (nums[writer] != val) {
        writer++;
      } else {
        if (nums[reader] != val) {
          //swap data
          int temp = nums[writer];
          nums[writer] = nums[reader];
          nums[reader] = temp;
          writer++;
        }
      }

      reader++;
    }

    print(writer);
    return writer;
  }
}
