class Solution {
    bool isAlNum(String char) {
        if (char.length != 1) return false;
        int codeUnit = char.codeUnitAt(0);
        return (codeUnit >= 65 && codeUnit <= 90) || // Büyük harf
        (codeUnit >= 97 && codeUnit <= 122) || // Küçük harf
        (codeUnit >= 48 && codeUnit <= 57);    // Rakam

    }


  bool isPalindrome(String s) {
    int l = 0;
    int r = s.length -1;

    while(l < r){
        // Move pointers until pointing an alphanumeric char.
        while (!isAlNum(s[l]) && l < r) {l++;}
        while (!isAlNum(s[r]) && l < r) {r--;}


        // Compare letter, if find a non-matching, early return false;
        if (s[l].toLowerCase() != s[r].toLowerCase()) {
            return false;
        }
        l++;
        r--;
    }

    return true;

  }
}