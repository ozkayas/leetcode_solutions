class Solution {
  int removeElement(List<int> nums, int val) {

      nums.removeWhere(
          (n) => n == val
      );

      return nums.length;
    
  }
}