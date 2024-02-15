class Solution {
  List<int> rearrangeArray(List<int> nums) {
      var pos = [];   /// [ 3, 2, 1]
      var neg = [];
      int p = 0;
      int n = 0;

        for(int n in nums){    //O(n)
            n > 0 ? pos.add(n) : neg.add(n);
        }
        // print(pos);
        // print(neg);
        for(int i=0; i<nums.length; i++){  //O(n)
            if(i.isEven){ //positif olmasi gereken index
                nums[i] = pos[p];  // okuma O(n)
                p++;  
            } else {
                nums[i] = neg[n];
                n++;
            }
        }

    return nums;
    
  }
}