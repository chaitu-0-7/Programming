# Link to problem: https://leetcode.com/problems/symmetric-tree/

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Example 1:

# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Example 2:

# Input: root = [1,2,2,null,3,null,3]
# Output: false

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def func(l,r):
            if l is None and r is None: return True
            if l is None and r!=None:return False
            if l!=None and r is None:return False
            if l.val!=r.val:return False
            return func(l.left,r.right) and func(l.right,r.left)
        if root is None:return True
        return func(root.left,root.right)