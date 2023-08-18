import 'dart:math';

main() {
  var num = 14;
  var result = SolutionII().numberOfSteps(num);
  // var result = Solution().numberOfSteps(num);
  return 0;
}

/// My first solution with recursion
class Solution {
  int numberOfSteps(int num) {
    int counter = 0;

    int reducer(int i) {
      if (i == 0) return 0;

      counter++;
      if (1 == 0) {
        return 0;
      } else {
        return (i.isEven) ? reducer(i ~/ 2) : reducer(i - 1);
      }
    }

    reducer(num);
    return counter;
  }
}

/// Solution using bitwise operation
class SolutionII {
  int numberOfSteps(int num) {
    int counter = 0;

    while (num > 0) {
      // checking even number, using 1 as bitmask
      if (num & 1 == 0) {
        num = num >> 1; // halving the num by shifting bits to right 1 step
      } else {
        num--;
      }
      counter++;
    }
    return counter;
  }
}
