# Link to Problem : https://leetcode.com/problems/balanced-binary-tree/

# Given a binary tree, determine if it is 
# height-balanced

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: true

# Example 2:

# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false

# Example 3:

# Input: root = []
# Output: true

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def func(root):
            if root is None:
                return True,0
            isleft,lh=func(root.left)
            isright,rh=func(root.right)
            if isleft and isright and abs(lh-rh)<=1:return True,max(lh,rh)+1
            return False,0
        ans,h=func(root)
        return ans