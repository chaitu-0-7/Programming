# Link to Problem: https://leetcode.com/problems/binary-tree-postorder-traversal/
# Given the root of a binary tree, return the postorder traversal of its nodes' values.

# Example 1:


# Input: root = [1,null,2,3]
# Output: [3,2,1]

# Example 2:

# Input: root = []
# Output: []

# Example 3:

# Input: root = [1]
# Output: [1]

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def func(root,out):
            if root is None:
                return
            func(root.left,out)
            func(root.right,out)
            out.append(root.val)
        out=[]
        func(root,out)
        return out