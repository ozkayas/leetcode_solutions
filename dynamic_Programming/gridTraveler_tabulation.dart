void main() {
  print(gridTraveler(1, 1));
  print(gridTraveler(2, 3));
  print(gridTraveler(3, 2));
  print(gridTraveler(18, 18));
}

int gridTraveler(int m, int n) {
  List<List<int>> table = List.generate(m + 1, (i) => List.generate(n + 1, (i) => 0));
  table[1][1] = 1;
  for (int i = 0; i <= m; i++) {
    for (int j = 0; j <= n; j++) {
      final current = table[i][j];
      if (j < n) {
        table[i][j + 1] += current;
      }
      if (i < m) {
        table[i + 1][j] += current;
      }
    }
  }

  return table[m][n];
}
