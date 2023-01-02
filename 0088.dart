main() {
  Solution().merge(
    [1, 2, 3, 0, 0, 0],
    3,
    [2, 5, 6],
    3,
  );
}

class Solution {
  void merge(List<int> nums1, int m, List<int> nums2, int n) {
    int pointer1 = m - 1;
    int pointer2 = n - 1;
    int end = nums1.length - 1;

    while (pointer1 >= 0 && pointer2 >= 0) {
      if (nums1[pointer1] > nums2[pointer2]) {
        nums1[end] = nums1[pointer1];
        pointer1--;
      } else {
        nums1[end] = nums2[pointer2];
        pointer2--;
      }
      end--;
    }

    while (pointer2 >= 0) {
      nums1[end] = nums2[pointer2];
      end--;
      pointer2--;
    }
  }
}
