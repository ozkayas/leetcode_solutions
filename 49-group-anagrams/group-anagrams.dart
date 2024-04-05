class Solution {
  List<List<String>> groupAnagrams(List<String> strs) {
    Map<String, List<String>> hMap = Map();


    for ( var s in strs){

        var sSorted = s.split("")..sort();
        // sSorted.sort();
        var sKey = sSorted.join("");

        (hMap[sKey] ??= []).add(s);
        // hMap.putIfAbsent(sKey, ()=>[]).add(s);


    }

    return hMap.values.toList();


  }
}

// ["eat","tea","tan","ate","nat","bat"]

// keyForWord = "abt"
// hMap : 
//     aet : [eat,tea,ate]
//     ant : [tan, nat]
//     abt : [bat]

//     return hMap.value

// n: 10*4
// O(n2)
// sorting - m log m 
// O(n x m log m)