void main() {
  var nums = [0, 2, 1, 5, 3, 4];

  print(Solution().buildArray(nums));
}

class Solution {
  // List<int> buildArray(List<int> nums) {
  //   List<int> result = [];
  //
  //   for (int i in nums) {
  //     result.add(nums[i]);
  //   }
  //
  //   return result;
  // }

  List<int> buildArray(List<int> nums) {
    int i = 0;
    for (int num in nums) {
      var barrelValue = ((nums[num] % 1000) * 1000) + (num % 1000);
      nums[i] = barrelValue;
      i++;
    }
    for (int i = 0; i < nums.length; i++) {
      nums[i] = nums[i] ~/ 1000;
    }
    return nums;
  }
}
