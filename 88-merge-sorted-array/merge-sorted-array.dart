class Solution {
  void merge(List<int> nums1, int m, List<int> nums2, int n) {
      int a = m -1, b = n -1, w = m+n - 1;

        while (w >= 0){

            if(a < 0){
                nums1[w] = nums2[b];
                b--;
                
            }

            else if(b < 0 || nums1[a] >= nums2[b]){
                nums1[w] = nums1[a];
                a--;
            }else{
                nums1[w] = nums2[b];
                b--;
                if(b < 0){
                    return;
                }
            }
            w--;
        }




// a                                b
//    [1,1,1,1,2,3,5,6]    -   [1,1,1,5,6]
//         w
    /// b < 0 ise return nums1
    /// a < 0 ise nums1[w] = nums[b] - b-;





    //   int i = m;
    //   for (int n in nums2){
    //       nums1[i] = n;
    //       i ++;
    //   }
    //   nums1.sort();
    //     // print(nums1);

  }
}