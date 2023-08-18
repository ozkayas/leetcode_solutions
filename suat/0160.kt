package LeetCodeProblems


// * Example:
// * var li = ListNode(5)
// * var v = li.`val`
// * Definition for singly-linked list.
 class ListNode(var `val`: Int) {
      var next: ListNode? = null
 }

class Solution {
    fun getIntersectionNode(headA:ListNode?, headB:ListNode?):ListNode? {


        var p1 = headA
        var p2 = headB
        if(p1 == null || p2 == null) return null


        while(p1 != p2){
            if(p1 == null){
                p1 = headB
            }else{
                p1 = p1.next;
            }
            if(p2 == null){
                p2 = headA
            }else{
                p2 = p2.next
            }
            print(p1?.`val`)
            println(p2?.`val`)

        }
        return p1
    }
}