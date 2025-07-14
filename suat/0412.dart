
main() {
  int n = 15;
  Solution().fizzBuzz(n);
  return 0;
}

class Solution {
  Map<int, String> hashTable = <int, String>{
    3: "Fizz",
    5: "Buzz",
  };

  List<String> fizzBuzz(int n) {
    List<String> result = List<String>.filled(n, "");
    for (int i = 1; i <= n; i++) {
      String item = "";
      hashTable.forEach((key, value) {
        if (i % key == 0) {
          item += value;
        }
      });
      if (item.isEmpty) item = i.toString();
      result[i - 1] = item;
    }
    return result;
  }
}
