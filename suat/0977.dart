main() {
  Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]);
}

// This is the official solutin that marks numbers with - sign
class Solution {
  List<int> findDisappearedNumbers(List<int> nums) {
    for (int i = 0; i < nums.length; i++) {
      int absValue = nums[i].abs();
      nums[absValue - 1] = -1 * nums[absValue - 1].abs();
    }

    List<int> result = [];
    for (int i = 0; i < nums.length; i++) {
      if (nums[i] > 0) result.add(i + 1);
    }

    return result;
  }
}

// pointer value ve sütun eşleşiyorsa 0 la ve index arttır.
// Elindeki değerin sutununu al ve orasını 0 ile işaretle - oradakini al
// gelen değer 0 ise gönderme yapma ve index arttır, else üst satır tekrarla
// geçtiğin değer 0 ise index arttır.
//
// 1, 2, 3, 4, 5, 6, 7, 8
// ----------------------
// 4, 3, 2, 7, 8, 2, 3, 1
// 7, 3, 2, 0, 8, 2, 3, 1
// 3, 3, 2, 0, 8, 2, 0, 1
// 2, 3, 0, 0, 8, 2, 0, 1
// 3, 2, 0, 0, 8, 2, 0, 1 - 3.sutunda 0 geldi, index arttır.
// 3, 0, 0, 0, 8, 2, 0, 1
// 3, 0, 0, 0, 1, 2, 0, 0
// 0, 0, 0, 0, 3, 2, 0, 0
// 0, 0, 0, 0, 3, 2, 0, 0
