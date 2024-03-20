class Solution {
  bool isIsomorphic(String s, String t) {
    final Map<String, String> hMap = {};

    //For loop icerisinde false durumlar aranacak
    for(int i=0; i<s.length; i++){
        final ch = s[i];

        if(hMap.containsKey(ch)){

            if(hMap[ch] != t[i]){
                return false;
            }

        }else{
            //Ilk kez rastladik
            if(hMap.containsValue(t[i])){
                return false;
            }

            hMap[ch] = t[i];

        }


    }

    return true;
    
  }
}



// "paper", t = "titli"
// ilk rastladigimizda mapleme, if t[i] already in hMap -> return false

// ikinci rastlamada map'e uygunluk kontrolu if NOT OK => false
// p:t
// a:i
// e:l
// r:i

