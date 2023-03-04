void main() {
  print(canConstruct("abcdef", ['ab', 'abc', 'cd', 'def', 'abcd'])); //true
  print(canConstruct("skateboard", ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])); //false
  print(canConstruct("enterapotentpot", ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])); //true
}

bool canConstruct(String target, List<String> wordBank) {
  final List<bool> table = List.generate(target.length + 1, (index) => index == 0 ? true : false);

  for (int i = 0; i <= target.length; i++) {
    // print(target.substring(0, i));
    if (table[i]) {
      for (var word in wordBank) {
        if (i + word.length <= target.length && target.indexOf(word, i) == i) {
          table[i + word.length] = true;
        }
      }
    }
  }

  print(table);
  return table[target.length];
}
