void main() {
  print(canConstruct("abcdef", ['ab', 'abc', 'cd', 'def', 'abcd'], {})); //true
  print(canConstruct("skateboard", ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], {})); //false
  print(canConstruct("enterapotentpot", ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'], {})); //true
}

/// recursive basic solution
// bool canConstruct(String target, List<String> wordBank) {
//   if (target == '') return true;
//
//   for (String word in wordBank) {
//     if (target.indexOf(word) == 0) {
//       var suffix = target.substring(word.length);
//       if (canConstruct(suffix, wordBank)) {
//         return true;
//       }
//     }
//   }
//   return false;
// }

bool canConstruct(String target, List<String> wordBank, Map<String, bool> memo) {
  if (memo.containsKey(target)) return memo[target]!;
  if (target == '') return true;

  for (String word in wordBank) {
    if (target.indexOf(word) == 0) {
      var suffix = target.substring(word.length);
      if (canConstruct(suffix, wordBank, memo)) {
        memo[target] = true;
        return true;
      }
    }
  }
  memo[target] = false;
  return false;
}
