import 'dart:math';

main() {
  Solution().thirdMax([1, 2, 1, 4, 5, 5, 5, 3]);
}

class Solution {
  int thirdMax(List<int> nums) {
    int lowerBound = nums.first;

    List<int> list = <int>[];

    for (int i in nums) {
      if (list.contains(i)) {
        continue;
      }
      //fill the list with 3 distinct numbers firstly
      if (list.length < 3) {
        list.add(i);
        lowerBound = min(lowerBound, i);
      } else if (i > lowerBound) {
        list.remove(lowerBound);
        list.add(i);
        lowerBound = min(list[0], min(list[1], list[2]));
      }
    }
    if (list.length == 1) return list.first;
    if (list.length == 2) return max(list[0], list[1]);
    return lowerBound;
  }
}
