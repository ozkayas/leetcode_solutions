void main() {
  // print(allConstruct("hello", ['cat', 'dog', 'mouse'], {})); // []
  // print(allConstruct("", ['cat', 'dog', 'mouse'], {})); // [[]]
  print(allConstruct("purple", ['purp', 'p', 'ur', 'le', 'purpl'], {})); // [purp, le] [p, ur, p ,le]
  print(allConstruct("abcdef", ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c'], {})); //true
  // print(allConstruct("skateboard", ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], {})); //false
  // print(allConstruct("enterapotentpot", ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'], {})); //true
}

/// recursive basic solution
// List<List<String>> allConstruct(String target, List<String> wordBank, Map memo) {
//   if (target == '') return [[]];
//
//   List<List<String>> result = [];
//
//   for (String word in wordBank) {
//     if (target.indexOf(word) == 0) {
//       var suffix = target.substring(word.length);
//       var suffixWays = allConstruct(suffix, wordBank, memo);
//       var targetWays = suffixWays.map((way) => [word, ...way]).toList();
//       result.addAll(targetWays);
//     }
//   }
//   return result;
// }

List<List<String>> allConstruct(String target, List<String> wordBank, Map memo) {
  if (memo.containsKey(target)) return memo[target];
  if (target == '') return [[]];

  List<List<String>> result = [];

  for (String word in wordBank) {
    if (target.indexOf(word) == 0) {
      var suffix = target.substring(word.length);
      var suffixWays = allConstruct(suffix, wordBank, memo);
      var targetWays = suffixWays.map((way) => [word, ...way]).toList();
      result.addAll(targetWays);
    }
  }
  memo[target] = result;
  return result;
}
