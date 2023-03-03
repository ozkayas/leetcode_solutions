/// howSum (7, [5,3,4,7]) => true
///
void main() {
  print(
    howSum(7, [2, 3]),
  );
  print(howSum(7, [5, 3, 4, 7]));
  print(howSum(7, [2, 4]));
  print(howSum(8, [2, 3, 5]));
  print(howSum(300, [7, 14]));
}

List<int>? howSum(int targetSum, List<int> numbers) {
  final List<List<int>?> table = List.filled(targetSum + 1, null);
  table[0] = [];

  for (int i = 0; i <= targetSum; i++) {
    for (int num in numbers) {
      if (table[i] != null && i + num <= targetSum) {
        table[i + num] = [...table[i]!, num];
      }
    }
  }

  // print(table);
  return table[targetSum];
}
