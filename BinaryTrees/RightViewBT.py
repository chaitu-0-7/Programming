# Link to Problem: https://leetcode.com/problems/binary-tree-right-side-view/

# Given the root of a binary tree, imagine yourself standing on the right side of it, 
# return the values of the nodes you can see ordered from top to bottom.

# Example 1:


# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
# Example 2:

# Input: root = [1,null,3]
# Output: [1,3]
# Example 3:

# Input: root = []
# Output: []

from queue import Queue
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        q=Queue()
        q.put(root)
        out=[]
        while q.qsize()>0:
            n=q.qsize()
            for i in range(n):
                temp=q.get()
                if i==n-1:
                    out.append(temp.val)
                if temp.left!=None:q.put(temp.left)
                if temp.right!=None:q.put(temp.right)
        return out