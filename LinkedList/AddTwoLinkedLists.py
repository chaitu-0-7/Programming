# Link to Problem: https://leetcode.com/problems/add-two-numbers/description/
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

class Solution:
    def addTwoNumbers(self, rev1: Optional[ListNode], rev2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        head=None
        while(rev1 is not None or rev2 is not None):
            a,b=0,0
            if rev1:
                a=rev1.val
            if rev2:
                b=rev2.val
            k=a+b+carry
            if head is None:
                head=ListNode(k%10)
                carry=k//10
                temp=head
            else:
                temp.next=ListNode(k%10)
                carry=k//10
                temp=temp.next
            if rev1:
                rev1=rev1.next
            if rev2:
                rev2=rev2.next
        if carry:
            temp.next=ListNode(carry)
            temp=temp.next
        return head