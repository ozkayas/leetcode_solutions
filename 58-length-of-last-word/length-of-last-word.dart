class Solution {
  int lengthOfLastWord(String s) {
        int p = s.length -1;
        
        // Son Elemani Bul
        while (s[p] == " "){
            p--;  
        }
        int lastCharOfLastWord = p;

        // Ilk bosluga rastlayana kadar sola ilerle
        while (p >=0 && s[p] != " "){
            p--;
        }
        int firstCharOfLastWord = p;


      return lastCharOfLastWord - firstCharOfLastWord;
  }
}

