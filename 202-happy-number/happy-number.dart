class Solution {
  // Two Pointers cozumu
  int sumOfSquares(int n){
    int sum = 0;
    while (n>0){
      int lastDigit = n %10;
      sum += lastDigit * lastDigit;
      n = n ~/ 10;
    }
    return sum;
  }

  bool isHappy(int n){
    //Edge case check
    if(sumOfSquares(n) == 1){
      return true;
    }

    int fast = n;
    int slow = n;

    while (fast != 1){
      fast = sumOfSquares(sumOfSquares(fast));
      slow = sumOfSquares(slow);
      if (fast == slow){
        return false;
      }
    }
    return true;
  }


  /// HashMap , Set cozumu
  // final isSeen = Set();

  //   return sum;
  // }

  // bool isHappy(int n) {
  //   isSeen.add(n);
  //   int curNumber = n;

  //   while(curNumber != 1){
  //     //karelerini toplave yeni curNumber
  //     curNumber = sumOfSquares(curNumber);

  //     // Dongu kontorlu yapalim
  //     if(isSeen.contains(curNumber)){
  //       return false;
  //     }{
  //       isSeen.add(curNumber);
  //     }

  //   }

  //   return true;
    
  // }
}