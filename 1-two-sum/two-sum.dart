// import 'dart:collections';
class Solution {
  List<int> twoSum(List<int> nums, int target) {
    final Map<int, dynamic> hMap = Map();

    for (int i = 0; i < nums.length; i++){
        int curr = nums[i];
        int partner = target - curr;

        if (hMap.containsKey(partner)){
            return [hMap[partner], i];
        } else {
            hMap[curr] = i;
        }
    }
    return [];
  }
}

// hMap : #partnerleri tutacak
//     2: 0
//     11: 1
//     15: 2



// [2,11,15, 7], target = 9
//           ^
//     return [hMap[9-7],i]

