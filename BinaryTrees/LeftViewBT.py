# Link to problem: https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/1

# Given a Binary Tree, print Left view of it. Left view of a Binary Tree is set of nodes visible when tree is visited from Left side. The task is to complete the function leftView(), which accepts root of the tree as argument.

# Left view of following tree is 1 2 4 8.

#           1
#        /     \
#      2        3
#    /     \    /    \
#   4     5   6    7
#    \
#      8   

# Example 1:

# Input:
#    1
#  /  \
# 3    2
# Output: 1 3

def func(root,level,out):
    if root is None:return
    if len(out)==level:
        out.append(root.data)
    func(root.left,level+1,out)
    func(root.right,level+1,out)
def LeftView(root):
    
    # code here
    out=[]
    func(root,0,out)
    return out