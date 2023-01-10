# Link to Problem: https://leetcode.com/problems/rotate-list/description/

# Given the head of a linked list, rotate the list to the right by k places.

# Example 1:

# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

# Example 2:

# Input: head = [0,1,2], k = 4
# Output: [2,0,1]

def size(head):
        count=0
        while(head is not None):
            count+=1
            head=head.next
        return count
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:return head        
        if head.next is None:return head
        n=size(head)
        k=k%n
        if k==0:return head
        n-=k
        temp=head
        while(n>1):
            n-=1
            temp=temp.next
        ans=temp.next
        temp.next=None
        temp=ans
        while(temp.next!=None):
            temp=temp.next
        temp.next=head
        return ans