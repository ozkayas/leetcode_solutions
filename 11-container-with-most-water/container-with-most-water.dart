import 'dart:math';

class Solution {
  int maxArea(List<int> height) {

    int l = 0;
    int r = height.length-1;

    int water =0;
    int curWater = 0;

    while(l < r){
        curWater = (r-l) * min(height[l], height[r]);
        water = max(water, curWater);

        if (height[l] < height[r]){
            l++;
        }else{
            r--;
        }
    }
    return water;
  }
}