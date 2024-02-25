class Solution {
  void rotate(List<int> nums, int k) {
      k = k % nums.length;

        reverse(nums, 0, nums.length-1);
        reverse(nums, 0 , k-1);
        reverse(nums, k , nums.length-1);
    //   var end = nums.sublist(nums.length-k, nums.length);
    //   var start = nums.sublist(0, nums.length-k);
    // //   print('$end, $start');
    //     List.copyRange(nums, 0, [...end,...start]);
    
  }

  void reverse(List<int> nums, int s , int e){

      while (s < e){
          var temp = nums[s];
          nums[s] = nums[e];
          nums[e] = temp;
          s++;
          e--;
      }

  }
}