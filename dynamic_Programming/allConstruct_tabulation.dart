void main() {
  print(allConstruct("hello", ['cat', 'dog', 'mouse'])); // []
  print(allConstruct("", ['cat', 'dog', 'mouse'])); // [[]]
  print(allConstruct("purple", ['purp', 'p', 'ur', 'le', 'purpl'])); // [purp, le] [p, ur, p ,le]
  print(allConstruct("abcdef", ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c'])); //true
  print(allConstruct("skateboard", ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])); //false
  print(allConstruct("enterapotentpot", ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])); //true
}

List<List<String>> allConstruct(String target, List<String> wordBank) {
  final List<List<List<String>>> table = List.generate(target.length + 1, (index) => index == 0 ? [[]] : []);

  for (int i = 0; i <= target.length; i++) {
    for (String word in wordBank) {
      if (i + word.length <= target.length && target.indexOf(word, i) == i) {
        // table[i + word.length] += table[i];
        var newCombinations = table[i].map((subArray) => [...subArray, word]).toList();
        table[i + word.length].addAll(newCombinations);
      }
    }
  }

  return table[target.length];
}
