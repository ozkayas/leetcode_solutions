class Solution {
  List<int> getFirsts(Set numsSet) {
    final firsts = <int>[];
    for (int item in numsSet) {
        if (!numsSet.contains(item-1)){
            firsts.add(item);
        }
    }

    return firsts;
  }



  int longestConsecutive(List<int> nums) {
    final numsSet = Set.from(nums);
    final firsts = getFirsts(numsSet);
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