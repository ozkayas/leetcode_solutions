class Solution {

int removeDuplicates(List<int> nums) {
  if (nums.isEmpty) return 0; // Handle the edge case where the list is empty

  int writeIndex = 0; // Initialize the write index to 0

  for (int i = 0; i < nums.length; i++) {
    if (writeIndex < 2 || nums[i] != nums[writeIndex - 2]) {
      // If the write index is less than 2 or the current element is different from
      // the element two positions before the write index
      nums[writeIndex] = nums[i]; // Overwrite the write index with the current number
      writeIndex++; // Move the write index forward
    }
  }

  return writeIndex; // Return the length of the modified list
}

}

// herhangi bir sayiya 2. kez denk gelirsek w++ ve ustune yaz
// ayni sayiya 2. ken denk geldigimi bilmek iicn bir map tutacagiz.

//                    r
// [0,0,1,1,2,3,3,3,3]
//              w