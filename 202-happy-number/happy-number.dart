class Solution {
  final isSeen = Set();

  int sumOfSquares(int n){
    int sum = 0;
    while (n>0){
      int lastDigit = n %10;
      sum += lastDigit * lastDigit;
      n = n ~/ 10;
    }

    return sum;
  }

  bool isHappy(int n) {
    isSeen.add(n);
    int curNumber = n;

    while(curNumber != 1){
      //karelerini toplave yeni curNumber
      curNumber = sumOfSquares(curNumber);

      // Dongu kontorlu yapalim
      if(isSeen.contains(curNumber)){
        return false;
      }{
        isSeen.add(curNumber);
      }

    }

    return true;
    
  }
}