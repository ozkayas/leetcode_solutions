/// howSum (7, [5,3,4,7]) => true
///
void main() {
  print(
    howSum(7, [2, 3], {}),
  );
  print(howSum(7, [5, 3, 4, 7], {}));
  print(howSum(7, [2, 4], {}));
  print(howSum(8, [2, 3, 5], {}));
  print(howSum(300, [7, 14], {}));
}

/// recursive basic solution
List<int>? howSum(int targetSum, List<int> numbers, Map<int, List<int>?> memo) {
  if (memo.containsKey(targetSum)) return memo[targetSum];
  if (targetSum == 0) return [];
  if (targetSum.isNegative) {
    memo[targetSum] = null;
    return null;
  }

  for (int num in numbers) {
    int remainder = targetSum - num;

    if (howSum(remainder, numbers, memo) != null) {
      memo[targetSum] = [...howSum(remainder, numbers, memo)!, num];
      return memo[targetSum];
    }
  }
  memo[targetSum] = null;
  return null;
}
