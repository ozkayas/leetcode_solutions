class Solution {
  void merge(List<int> nums1, int m, List<int> nums2, int n) {
      int i = m;
      for (int n in nums2){
          nums1[i] = n;
          i ++;
      }
      nums1.sort();
        // print(nums1);

  }
}