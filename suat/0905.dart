main() {
  Solution().sortArrayByParity([1, 3]);
}

class Solution {
  List<int> sortArrayByParity(List<int> nums) {
    int head = 0;
    int tail = nums.length - 1;

    while (head < tail) {
      if (nums[head].isOdd) {
        if (nums[tail].isEven) {
          //swap values
          int temp = nums[head];
          nums[head] = nums[tail];
          nums[tail] = temp;
          head++;
          tail--;
        } else {
          tail--;
        }
      } else {
        head++;
      }
    }

    return nums;
  }
}
