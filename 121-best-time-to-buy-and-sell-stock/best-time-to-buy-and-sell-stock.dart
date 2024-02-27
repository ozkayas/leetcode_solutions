class Solution {
  int maxProfit(List<int> prices) {
    int l = 0, r=0;
    int maxP = 0;

    while(r < prices.length){

      if(prices[r]<prices[l]){
        l = r;
      }

      int curP = prices[r] - prices[l];
      maxP = curP > maxP ? curP : maxP;  // maxP = max(maxP, curP)  import 'dart:math';



      r++;
    }


    return maxP;
  }
}
