# Link to Problem: https://leetcode.com/problems/binary-tree-level-order-traversal/

# Given the root of a binary tree, return the level order traversal of its nodes' 
# values. (i.e., from left to right, level by level).

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# Example 2:

# Input: root = [1]
# Output: [[1]]

# Example 3:

# Input: root = []
# Output: []

from queue import Queue
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:return[]
        q=Queue()
        q.put(root)
        out=[]
        while q.qsize()>0:
            temp=[]
            n=q.qsize()
            for i in range(n):
                t=q.get()
                temp.append(t.val)
                if t.left:q.put(t.left)
                if t.right:q.put(t.right)
            out.append(temp)
        return out