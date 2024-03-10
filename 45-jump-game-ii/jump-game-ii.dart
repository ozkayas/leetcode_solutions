class Solution {
  int jump(List<int> nums) {
      int p = 0;
      List<int> jumps = List.filled(nums.length, 0);

      while(p < nums.length){
          for(int i = 1; i <= nums[p]; i++ ){
              int scanner = p + i;
              if(scanner == nums.length-1){
                  return jumps[scanner] = jumps[p]+1;
              }
              if (scanner >= nums.length){
                  break;
              }
              if (jumps[scanner] == 0){
                  jumps[scanner] = jumps[p]+1;
              }

          }

          p++;
      }
      return jumps.last;

    
  }
}


//  0 1         2
// [2,5,1,0,1,2,4]
//            |