/// canSum (7, [5,3,4,7]) => true
///
void main() {
  print(
    canSum(7, [2, 3], {}),
  );
  print(canSum(7, [5, 3, 4, 7], {}));
  print(canSum(7, [2, 4], {}));
  print(canSum(8, [2, 3, 5], {}));
  print(canSum(300, [7, 14], {}));
}

/// recursive basic solution
// bool canSum(int targetSum, List<int> numbers) {
//   if (targetSum == 0) return true;
//   if (targetSum.isNegative) return false;
//
//   for (int num in numbers) {
//     if (canSum(targetSum - num, numbers)) {
//       return true;
//     }
//   }
//   return false;
// }

bool canSum(int targetSum, List<int> numbers, Map<int, bool> memo) {
  if (memo.containsKey(targetSum)) return memo[targetSum]!;
  if (targetSum == 0) return true;
  if (targetSum.isNegative) return false;

  for (int num in numbers) {
    if (canSum(targetSum - num, numbers, memo)) {
      memo[targetSum] = true;
      return true;
    }
  }
  memo[targetSum] = false;
  return false;
}
