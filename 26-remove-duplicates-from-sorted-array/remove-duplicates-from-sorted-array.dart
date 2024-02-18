class Solution {
  int removeDuplicates(List<int> nums) {

      final s = nums.toSet();
    //   print(s);
      final l = s.toList();
      l.sort();
    //   print(l);

    for (int i = 0; i < l.length; i++){
        nums[i] = l[i];
    }
    
    
    return l.length;
  }
}