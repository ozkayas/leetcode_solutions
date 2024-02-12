class Solution {
  int lengthOfLastWord(String s) {
      final arr = s.trim().split(' ');
    //   print(arr);
    //   print(arr.last);

      return arr.last.length;
  }
}