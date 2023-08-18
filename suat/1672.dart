import 'dart:math';

main() {
  var accounts = [
    [2, 8, 7],
    [7, 1, 3],
    [1, 9, 5]
  ];
  var result = Solution().maximumWealth(accounts);
  return 0;
}

class Solution {
  int maximumWealth(List<List<int>> accounts) {
    int maxValue = 0;
    for (List<int> customer in accounts) {
      int customersTotalMoney = 0;
      for (int money in customer) {
        customersTotalMoney += money;
      }
      maxValue = max(maxValue, customersTotalMoney);
    }
    return maxValue;
  }
}
