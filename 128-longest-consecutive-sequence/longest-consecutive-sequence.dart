class Solution {
  List<int> getFirsts(List<int> nums){
    final numsSet = Set.from(nums);
    final firsts = <int>[];
    for (int item in numsSet){
        if(!numsSet.contains(item-1)){
            firsts.add(item);
        }
    }
    return firsts;
  }


  int longestConsecutive(List<int> nums) {
    final firsts = getFirsts(nums);
    final numsSet = Set.from(nums);
    int longest = 0;

    for (int val in firsts){
        int counter = 1;
        while (numsSet.contains(val+1)){
            counter ++;
            val ++;
        }
        longest = max(longest, counter);
    }
    return longest;

  }
}


// [100,4,200,1,3,2,99]
// -> 1 2 3 4
// -> 99 100
// -> 200

// Firsts, Zincir baslangiclarini bul -> 1 , 99 , 200

// firsts listesi loop cevir, enUzun degisteknini gguncelle