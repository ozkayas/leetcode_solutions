class Solution {
  int majorityElement(List<int> nums) {
      var map = {};
      int res = 0;

      for(int n in nums){
          map[n] = 1 + (map[n] ?? 0);

            if(map[n] > nums.length/2){
                res = n;
                break;
            }

      }
    
    return res;
  }
}