# Link to Problem: https://www.interviewbit.com/problems/path-to-given-node/

# Problem Description

# Given a Binary Tree A containing N nodes.

# You need to find the path from Root to a given node B.

# NOTE:

# No two nodes in the tree have same data values.
# You can assume that B is present in the tree A and a path always exists.

# Input 1:

#  A =

#            1
#          /   \
#         2     3
#        / \   / \
#       4   5 6   7 


# B = 5

# Input 2:

#  A = 
#             1
#           /   \
#          2     3
#         / \ .   \
#        4   5 .   6


# B = 1

# Example Output
# Output 1:

#  [1, 2, 5]

# Output 2:

#  [1]

# Example Explanation
# Explanation 1:

#  We need to find the path from root node to node with data value 5.
#  So the path is 1 -> 2 -> 5 so we will return [1, 2, 5]
# Explanation 2:

#  We need to find the path from root node to node with data value 1.
#  As node with data value 1 is the root so there is only one node in the path.
#  So we will return [1]

 class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        def func(root,target,out):
            if root is None:
                return False
            if root.val==target:
                out.append(root.val)
                return True
            if func(root.left,target,out):
                out.append(root.val)
                return True
            if func(root.right,target,out):
                out.append(root.val)
                return True
            return False
        out=[]
        func(A,B,out)
        return out[::-1]