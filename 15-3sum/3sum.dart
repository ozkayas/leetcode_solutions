class Solution {
  List<List<int>> threeSum(List<int> nums) {
    nums.sort();
    List<List<int>> ans = [];

    //Ana for loop
    for (int i = 0; i < nums.length-2; i++){
        // Ayni sayiyi tekrar etmemek icin
        if (i > 0 && nums[i] == nums[i-1]) continue;

        // Alt dizide 2 sum ariyoruz
        int l = i+1;
        int r = nums.length-1;
        int target = -nums[i];

        while (l < r){
            int sum = nums[l] + nums[r];
            if(sum < target){
                l++;
            }else if(sum > target){
                r--;
            }else{
                //Cozum bulundu
                ans.add([nums[i],nums[l],nums[r]]);
                int curL = nums[l];
                int curR = nums[r];

                while (l < r && nums[l] == curL) l++;
                while (l < r && nums[r] == curR) r--;
            }
        }
    }
    return ans;
    
  }
}