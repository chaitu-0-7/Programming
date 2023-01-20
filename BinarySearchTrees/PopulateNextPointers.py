# Link to Problem: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

# You are given a perfect binary tree where all leaves are on the same level,
#  and every parent has two children. The binary tree has the following definition:

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

# Example 1:

# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]
# Explanation: Given the above perfect binary tree (Figure A), your function should populate
#  each next pointer to point to its next right node, just like in Figure B. The serialized output 
#  is in level order as connected by the next pointers, with '#' signifying the end of each level.

# Example 2:

# Input: root = []
# Output: []

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None: return root
        cur,nex=root,root.left
        while cur and nex:
            cur.left.next=cur.right
            if cur.next:
                cur.right.next=cur.next.left
            cur=cur.next
            if cur==None:
                cur=nex
                nex=cur.left
        return root

from queue import Queue
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:return
        q=Queue()
        q.put(root)
        while q.qsize()>0:
            n=q.qsize()
            # temp=q.get()
            for i in range(n):
                if i==0:
                    temp=q.get()
                else:
                    nex=q.get()
                    temp.next=nex
                    temp=nex
                if temp.left:q.put(temp.left)
                if temp.right:q.put(temp.right)
            temp.next=None
        return root