class Solution {
  int removeElement(List<int> nums, int val) {

      int w = 0 ;
      int r = 0 ;

      while (r < nums.length){

          //OK degere rastlar isek bunu yazacagiz
          if(nums[r] != val){
              nums[w] = nums[r];
              w++;
            //   nums[r] = -1
          }

          r++;
      }
      print(nums);
      return w;


    //   nums.removeWhere(
    //       (n) => n == val
    //   );

    //   return nums.length;
    
  }
}


