# Link to Problem: https://leetcode.com/problems/palindrome-linked-list/
# Given the head of a singly linked list, return true if it is a 
# palindrome or false otherwise.
 

# Example 1:

# Input: head = [1,2,2,1]
# Output: True

# Example 2:

# Input: head = [1,2]
# Output: false

def reverse(head):
    prev=None
    cur=head
    while(cur is not None):
        t=cur.next
        cur.next=prev
        prev=cur
        cur=t
    return prev
def mid(head):
    slow=head
    fast=head
    while(fast!=None and fast.next!=None):
        slow=slow.next
        fast=fast.next.next
        prev=slow
    return prev,slow
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev,m=mid(head)
        prev.next=None
        prev.next=reverse(m)
        d=head
        m=prev.next
        while(m!=None):
            if m.val==d.val:
                m=m.next
                d=d.next
            else:return False
        return True