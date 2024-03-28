class Solution {
  bool wordPattern(String pattern, String s) {
    var sl = s.split(" ");
    if (sl.length != pattern.length){
        return false;
    }
    var sSet = Set();
    var pSet = Set();
    var combiSet = Set();

    for(int i=0; i<pattern.length; i++){
        pSet.add(pattern[i]);
        sSet.add(sl[i]);
        combiSet.add(pattern[i]+sl[i]);

        if(pSet.length != sSet.length || pSet.length != combiSet.length){
        return false;}
        
    }
    return true;
  }
}



// pattern = "abba", sl = "dog" "cat" "cat" "fish"

// pS : a , b 
// sS : dog , cat, fish
// combiSet : adog,  bcat , bfish



