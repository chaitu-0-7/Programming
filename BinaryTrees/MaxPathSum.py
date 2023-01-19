# Link to Problem: https://leetcode.com/problems/binary-tree-maximum-path-sum/

# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in 
# the sequence has an edge connecting them. A node can only appear in the sequence at most once. 
# Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, return the maximum path sum of any non-empty path.
# Example 1:

# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

# Example 2:

# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def func(root,ans):
            if root is None:return 0
            lh=func(root.left,ans)
            rh=func(root.right,ans)
            cur=root.val
            if lh>0:cur+=lh
            if rh>0:cur+=rh
            ans[0]=max(ans[0],cur)
            return max(max(lh,rh)+root.val,0)
        ans=[-1001]
        func(root,ans)
        return ans[0]