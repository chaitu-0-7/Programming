# Link to Problem: https://leetcode.com/problems/search-in-a-binary-search-tree/

# You are given the root of a binary search tree (BST) and an integer val.

# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. 
# If such a node does not exist, return null.

# Example 1:

# Input: root = [4,2,7,1,3], val = 2
# Output: [2,1,3]

# Example 2:

# Input: root = [4,2,7,1,3], val = 5
# Output: []

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def func(root,val):
            if root is None:return None
            if root.val==val:return root
            if val<root.val:return func(root.left,val)
            return func(root.right,val)
        return func(root,val)