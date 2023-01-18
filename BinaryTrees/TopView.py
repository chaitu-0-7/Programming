# Link to Problem: https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1

# Given below is a binary tree. The task is to print the top view of binary tree.
#  Top view of a binary tree is the set of nodes visible when the tree is viewed from the top. For the given below tree

#        1
#     /     \
#    2       3
#   /  \    /   \
# 4    5  6   7

# Top view will be: 4 2 1 3 7
# Note: Return nodes from leftmost node to rightmost node. Also if 2 nodes are outside the shadow of the tree and are at same position then consider the extreme ones only(i.e. leftmost and rightmost). 
# For ex - 1 2 3 N 4 5 N 6 N 7 N 8 N 9 N N N N N will give 8 2 1 3 as answer. Here 8 and 9 are on the same position but 9 will get shadowed.

# Example 1:

# Input:
#       1
#    /    \
#   2      3
# Output: 2 1 3
# Example 2:

# Input:
#        10
#     /      \
#   20        30
#  /   \    /    \
# 40   60  90    100
# Output: 40 20 10 30 100

from queue import Queue

class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        
        # code here
        q=Queue()
        q.put([root,0])
        d={}
        out=[]
        while q.qsize()>0:
            temp=q.get()
            if temp[1] not in d:
                d[temp[1]]=temp[0].data
            if temp[0].left:q.put([temp[0].left,temp[1]-1])
            if temp[0].right:q.put([temp[0].right,temp[1]+1])
        for i in sorted(d.keys()):
            out.append(d[i])
        return out