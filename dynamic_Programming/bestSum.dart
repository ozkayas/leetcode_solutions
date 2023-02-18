void main() {
  print(bestSum(7, [5, 3, 4, 7], {})); //7
  print(bestSum(8, [1, 4, 5], {})); // [4,4]
  print(bestSum(8, [2, 3, 5], {})); // [3,5]
  print(bestSum(100, [1, 2, 5, 25], {})); //[25,25,25,25]
}

/// recursive basic solution
// List<int>? bestSum(int targetSum, List<int> numbers, Map<int, List<int>?> memo) {
//   if (targetSum == 0) return [];
//   if (targetSum.isNegative) {
//     return null;
//   }
//
//   List<int>? shortestPath;
//
//   for (int num in numbers) {
//     int remainder = targetSum - num;
//     List<int>? remainderPath = bestSum(remainder, numbers, memo);
//
//     if (remainderPath != null) {
//       var currentPath = [...remainderPath, num];
//       if (shortestPath == null) {
//         shortestPath = currentPath;
//       } else {
//         if (currentPath.length < shortestPath.length) shortestPath = currentPath;
//       }
//     }
//   }
//   return shortestPath;
// }

/// recursive basic solution
List<int>? bestSum(int targetSum, List<int> numbers, Map<int, List<int>?> memo) {
  if (memo.containsKey(targetSum)) return memo[targetSum];
  if (targetSum == 0) return [];
  if (targetSum.isNegative) {
    return null;
  }

  List<int>? shortestPath;

  for (int num in numbers) {
    int remainder = targetSum - num;
    List<int>? remainderPath = bestSum(remainder, numbers, memo);

    if (remainderPath != null) {
      var currentPath = [...remainderPath, num];
      if (shortestPath == null) {
        shortestPath = currentPath;
      } else {
        if (currentPath.length < shortestPath.length) shortestPath = currentPath;
      }
    }
  }
  memo[targetSum] = shortestPath;
  return shortestPath;
}
