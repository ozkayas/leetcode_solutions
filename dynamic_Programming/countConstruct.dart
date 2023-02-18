import 'canSum.dart';

void main() {
  print(countConstruct("purple", ['purp', 'p', 'ur', 'le', 'purpl'], {})); // 2
  print(countConstruct("abcdef", ['ab', 'abc', 'cd', 'def', 'abcd'], {})); // 1
  print(countConstruct("skateboard", ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], {})); // 0
  print(countConstruct("enterapotentpot", ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'], {})); // 4
}

/// recursive basic solution
// int countConstruct(String target, List<String> wordBank, Map<String, int> memo) {
//   if (target == '') return 1;
//   int totalCount = 0;
//
//   for (String word in wordBank) {
//     if (target.indexOf(word) == 0) {
//       var suffix = target.substring(word.length);
//       var numWaysForRest = countConstruct(suffix, wordBank, memo);
//       totalCount += numWaysForRest;
//       // if (countConstruct(suffix, wordBank, memo)) {
//       //   return true;
//       // }
//     }
//   }
//   return totalCount;
// }

int countConstruct(String target, List<String> wordBank, Map<String, int> memo) {
  if (memo.containsKey(target)) return memo[target]!;
  if (target == '') return 1;
  int totalCount = 0;

  for (String word in wordBank) {
    if (target.indexOf(word) == 0) {
      var suffix = target.substring(word.length);
      var numWaysForRest = countConstruct(suffix, wordBank, memo);
      totalCount += numWaysForRest;
      // if (countConstruct(suffix, wordBank, memo)) {
      //   return true;
      // }
    }
  }
  memo[target] = totalCount;
  return totalCount;
}
