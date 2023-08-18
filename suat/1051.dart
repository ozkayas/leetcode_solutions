main() {
  Solution().heightChecker([1, 1, 4, 2, 1, 3]);
}

class Solution {
  int heightChecker(List<int> heights) {
    List<int> sorted = List.from(heights);
    sorted.sort();
    int diffCounter = 0;
    for (int i = 0; i < heights.length; i++) {
      if (heights[i] != sorted[i]) diffCounter++;
    }
    return diffCounter;
  }
}
