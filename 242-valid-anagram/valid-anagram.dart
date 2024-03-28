class Solution {
  bool isAnagram(String s, String t) {
    var map = Map();

    for(int i = 0; i<s.length; i++){
        map[s[i]] = 1 + (map[s[i]] ?? 0);
    }

    for(int i = 0; i<t.length; i++){
        if(map.containsKey(t[i])){
            if (map[t[i]] == 1) {
                map.remove(t[i]);
            }else{
                map[t[i]]--;
            }


        }else{
            return false;

        }
    }

    // print(map);
    return map.isEmpty;

  }
}