Link to Problem: https://leetcode.com/problems/binary-tree-inorder-traversal/
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out=[]
        def func(root,out):
            if root is None:
                return
            func(root.left,out)
            out.append(root.val)
            func(root.right,out)
        func(root,out)
        return out