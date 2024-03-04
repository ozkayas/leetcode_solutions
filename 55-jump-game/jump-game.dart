class Solution {
  bool canJump(List<int> nums) {
      int m =0 , p = 0;

      while(p <= m){
          if ( p + nums[p] > m){
              m = p + nums[p];
          }
          if (m >= nums.length-1){
              return true;
          }


          p++;
      }
      return false;
    
  }
}