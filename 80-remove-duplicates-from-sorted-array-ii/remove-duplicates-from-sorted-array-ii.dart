class Solution {
  int removeDuplicates(List<int> nums) {
        int r = 0, w = 0;
        var map = {};

        while(r < nums.length){
            if(!map.containsKey(nums[r]))
            {map.clear();}

            map[nums[r]] = (map[nums[r]] ?? 0) + 1;

            if(nums[r] > nums[w]){
                w++;
                nums[w] = nums[r];
                // map.clear();
            }

            if(nums[r] == nums[w] && map[nums[r]] == 2){
                w++;
                nums[w] = nums[r];  
                // map.clear(); 
            }

            r ++;
        }

    return w + 1;
  }
}

// herhangi bir sayiya 2. kez denk gelirsek w++ ve ustune yaz
// ayni sayiya 2. ken denk geldigimi bilmek iicn bir map tutacagiz.

//                    r
// [0,0,1,1,2,3,3,3,3]
//              w