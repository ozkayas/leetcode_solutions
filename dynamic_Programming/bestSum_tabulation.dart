void main() {
  print(bestSum(7, [5, 3, 4, 7])); //7
  print(bestSum(8, [1, 4, 5])); // [4,4]
  print(bestSum(8, [2, 3, 5])); // [3,5]
  print(bestSum(100, [1, 2, 5, 25])); //[25,25,25,25]
}

/// recursive basic solution
List<int>? bestSum(int targetSum, List<int> numbers) {
  final List<List<int>?> table = List.filled(targetSum + 1, null);
  table[0] = [];

  for (int i = 0; i <= targetSum; i++) {
    if (table[i] != null) {
      for (int num in numbers) {
        if (i + num <= targetSum) {
          final candidate = [...table[i]!, num];
          if (table[i + num] == null) {
            table[i + num] = candidate;
          } else if (candidate.length < table[i + num]!.length) {
            table[i + num] = candidate;
          }
        }
      }
    }
  }

  return table[targetSum];
}
