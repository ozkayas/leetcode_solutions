class Solution {
  int maxProfit(List<int> prices) {
      int profit = 0;

      for(int i = 0; i < prices.length -1; i++){
          int curP = prices[i+1] - prices[i];
          if(curP > 0){
              profit += curP;
          }
      }

      return profit;
    
  }
}