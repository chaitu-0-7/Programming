# Link to Problem: https://leetcode.com/problems/diameter-of-binary-tree/

# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
#  This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.


# Example 1:


# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

# Example 2:

# Input: root = [1,2]
# Output: 1

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def func(root,ans):
            if root is None:return 0
            lh=func(root.left,ans)
            rh=func(root.right,ans)
            ans[0]=max(ans[0],lh+rh)
            return max(lh,rh)+1
        ans=[0]
        func(root,ans)
        return ans[0]