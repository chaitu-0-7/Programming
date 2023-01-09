# Link to the Problem: https://leetcode.com/problems/reverse-linked-list/
# Given the head of a singly linked list, reverse the list, and return the reversed list.
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Input: head = [1,2]
# Output: [2,1]

# Input: head = []
# Output: []

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:return head
        if head.next is None:return head
        prev=None
        cur=head
        while(cur is not None):
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        return prev
        