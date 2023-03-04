void main() {
  print(countConstruct("purple", ['purp', 'p', 'ur', 'le', 'purpl'])); // 2
  print(countConstruct("abcdef", ['ab', 'abc', 'cd', 'def', 'abcd'])); // 1
  print(countConstruct("skateboard", ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])); // 0
  print(countConstruct("enterapotentpot", ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])); // 4
}

int countConstruct(String target, List<String> wordBank) {
  final List<int> table = List.generate(target.length + 1, (index) => index == 0 ? 1 : 0);

  for (int i = 0; i <= target.length; i++) {
    if (table[i] > 0) {
      for (String word in wordBank) {
        if (i + word.length <= target.length && target.indexOf(word, i) == i) {
          table[i + word.length] += table[i];
        }
      }
    }
  }

  return table[target.length];
}
