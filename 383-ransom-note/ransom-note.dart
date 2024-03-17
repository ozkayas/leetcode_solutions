class Solution {


  bool canConstruct(String ransomNote, String magazine) {
    Map<String, int> noteMap = {};
    Map<String, int> magazineMap = {};
    // Map strToFreq(String map){/////}

    for (int i = 0; i < ransomNote.length; i++){
        final char = ransomNote[i];

        if(noteMap.containsKey(char)){
            noteMap[char] = noteMap[char]! +1;
        }else{
            noteMap[char] = 1;
        }
    }

    for (int i = 0; i < magazine.length; i++){
        final char = magazine[i];

        if(magazineMap.containsKey(char)){
            magazineMap[char] = magazineMap[char]! + 1 ;
        }else{
            magazineMap[char] = 1;
        }
    }

    // print(noteMap);
    // print(magazineMap);

    for(var key in noteMap.keys){
        if(magazineMap.containsKey(key)){
            if (magazineMap[key]! < noteMap[key]!){
                return false;
            }
        }else{
            return false;
        }
    }
    return true;

  }
}

    // 2 adet frekans tutan hashMap 

    // loop over note map items - False durumari ara
        // bu karakter magazinde var mi? False
        // varsa - >  yeteri kadar degil ise : False

    // loop tan cikinca return true


// magazin :
//     a : 2
//     b : 1

// note: 
//     a : 2
//     c : 3