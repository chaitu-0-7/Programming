# Link to problem: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Given the root of a binary tree, flatten the tree into a "linked list":

# The "linked list" should use the same TreeNode class where the right child pointer points to 
# the next node in the list and the left child pointer is always null.
# The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 
# Example 1:

# Input: root = [1,2,5,3,4,null,6]
# Output: [1,null,2,null,3,null,4,null,5,null,6]

# Example 2:

# Input: root = []
# Output: []

# Example 3:

# Input: root = [0]
# Output: [0]

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def func(root):
            if root is None:return None,None
            head1,tail1=func(root.left)
            head2,tail2=func(root.right)
            if head1==None and head2==None:
                return root,root
            if head1==None:
                root.right=head2
                return root,tail2
            if head2==None:
                root.left=None
                root.right=head1
                return root,tail1
            root.right=head1
            tail1.right=head2
            root.left=None
            return root,tail2
        func(root)