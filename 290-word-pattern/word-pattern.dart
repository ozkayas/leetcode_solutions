class Solution {
  bool wordPattern(String pattern, String s) {
    var sl = s.split(" ");
    if (sl.length != pattern.length){
        return false;
    }
    var pSet = Set();
    var slSet = Set();
    var combiSet = Set();

    for (int i = 0; i < sl.length; i++){
        pSet.add(pattern[i]);
        slSet.add(sl[i]);
        combiSet.add(pattern[i]+sl[i]);

        if(pSet.length != slSet.length || pSet.length != combiSet.length){
            return false;
        }

    }
    return true;
    
  }
}


// "abba", sl = "dog" "cat" "cat" "fish"
//      |
// p : a, b
// sl : dog, cat, fish
// combi :  adog, bcat, afish