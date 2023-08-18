import 'dart:math';

main() {
  // var num = 14;
  // var result = Solution().middleNode();
  // var result = Solution().numberOfSteps(num);
  return 0;
}

class ListNode {
  int val;
  ListNode? next;
  ListNode([this.val = 0, this.next]);
}

//First solution
class Solution {
  ListNode? middleNode(ListNode? head) {
    if (head!.next == null) return head;
    //Move one step if possible and shift pointers. Because if tailPointer at 2, middlePointer should be at 2 also.
    // Then for each two step of tailPointer, middlePointer will shift 1 step.
    ListNode tailPointer = head.next!;
    ListNode middlePointer = head.next!;

    int stepCounter = 0;

    while (tailPointer.next != null) {
      tailPointer = tailPointer.next!;
      stepCounter++;
      if (stepCounter.isEven) {
        middlePointer = middlePointer.next!;
      }
    }

    return middlePointer;
  }
}

// Upgraded solution as per LeetCode solution
class SolutionII {
  ListNode? middleNode(ListNode? head) {
    ListNode? tailPointer = head;
    ListNode? middlePointer = head;

    while (tailPointer != null && tailPointer.next != null) {
      tailPointer = tailPointer.next!.next;
      middlePointer = middlePointer!.next;
    }

    return middlePointer;
  }
}

class SolutionIII {
  ListNode? middleNode(ListNode? head) {
    ListNode? tailPointer = head;
    ListNode? middlePointer = head;

    for (int i = 0; tailPointer != null && tailPointer.next != null; tailPointer = tailPointer.next!.next) {
      if ((i++).isEven) {
        middlePointer = middlePointer!.next;
      }
    }

    return middlePointer;
  }
}
