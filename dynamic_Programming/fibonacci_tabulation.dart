void main() {
  print(fib(6));
  print(fib(7));
  print(fib(8));
  print(fib(50));
}

int fib(int n) {
  List<int> table = List<int>.filled(n + 1, 0, growable: false);
  table[1] = 1;

  for (int i = 0; i <= n - 1; i++) {
    table[i + 1] += table[i];
    if (i <= n - 2) {
      table[i + 2] += table[i];
    }
  }
  return table[n];
}
