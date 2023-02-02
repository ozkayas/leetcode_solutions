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
        var p1headChanged = false
        var p2headChanged = false

        while(p1 != p2){
            if(p1?.next == null){
                if(p1headChanged){
                    return null

                }
                p1 = headB
                p1headChanged = true
            }else{
                p1 = p1.next
            }
            if(p2?.next == null){
                if(p2headChanged){
                    return null
                }
                p2 = headA
                p2headChanged = true
            }else{
                p2 = p2.next
            }
            print(p1?.`val`)
            println(p2?.`val`)

        }
        return p1
    }
}