import 'dart:math';

void main() {
  var nums = [2, 3, 5, 1, 3];

  print(Solution().kidsWithCandies(nums, 3));
}

class Solution {
  List<bool> kidsWithCandies(List<int> candies, int extraCandies) {
    List<bool> answer = [];
    var list = [...candies]..sort();
    var max = list.last;

    for (int num in candies) {
      answer.add(num + extraCandies >= max);
    }
    return answer;
  }
}
