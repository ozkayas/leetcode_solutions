void main() {
  print(canSum(7, [2, 3]));
  print(canSum(7, [2, 4]));
  print(canSum(7, [5, 3, 4, 7]));
  print(canSum(8, [5, 3, 2]));
  print(canSum(300, [7, 14]));
}

bool canSum(int targetSum, List<int> numbers) {
  final table = List.filled(targetSum + 1, false);
  table[0] = true;

  for (var i = 0; i <= targetSum; i++) {
    if (table[i]) {
      for (int num in numbers) {
        if (i + num <= targetSum) {
          table[i + num] = true;
        }
      }
    }
  }
  // print(table);
  return table[targetSum];
}
