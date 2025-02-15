class Solution {
  List<int> twoSum(List<int> numbers, int target) {
    int l = 0;
    int r  = numbers.length-1;

    while(l<r){
        int total = numbers[l] + numbers[r];
        if (total == target) break;

        if(total > target){
            r--;
        }else{
            l++;
        }

    }
    
    return [l+1,r+1];

  }
}
