class Solution {
  int removeDuplicates(List<int> nums) {

      int r = 0, w = 0;

      while(r < nums.length){
          if(nums[r] > nums[w]){
              w++;
              nums[w] = nums[r];
          }

          r ++;
      }

      return w + 1;


 // r ana while loopda sonra kadar gidecek
 // r > w ->  w++ , yazma islemi

//                       r
//  [0,1,2,3,4,2,2,3,3,4]
//           w

// return w + 1;







    //   final s = nums.toSet();
    // //   print(s);
    //   final l = s.toList();
    //   l.sort();
    // //   print(l);

    // for (int i = 0; i < l.length; i++){
    //     nums[i] = l[i];
    // }
    
    
    // return l.length;
  }
}