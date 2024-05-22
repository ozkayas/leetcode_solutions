class Solution {
  bool containsNearbyDuplicate(List<int> nums, int k) {
    // Save last index of a number
    final lastIndex = Map();
    final n = nums.length;

    for (int i=0; i < n; i++){
        final cur = nums[i];
        if (!lastIndex.containsKey(cur)){
            lastIndex[cur] = i;
        } else {
            // check if in the bounds
            if (i - lastIndex[cur] <= k){
                return true;
            }
            lastIndex[cur] = i;
        }
    }
    return false;

  }
}