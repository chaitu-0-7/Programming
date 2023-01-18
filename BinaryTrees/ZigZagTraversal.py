# Link to Problem: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Given the root of a binary tree, return the zigzag level order traversal of its nodes'
# values. (i.e., from left to right, then right to left for the next level and alternate between).


# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]

# Example 2:

# Input: root = [1]
# Output: [[1]]

# Example 3:

# Input: root = []
# Output: []

from queue import Queue
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        out=[]
        if root is None:return out
        q=Queue()
        q.put(root)
        flag=False
        while(q.qsize()>0):
            temp=[]
            n=q.qsize()
            for i in range(n):
                t=q.get()
                temp.append(t.val)
                if t.left:q.put(t.left)
                if t.right:q.put(t.right)
            if flag:
                out.append(temp[::-1])
                flag=False
            else:
                flag=True
                out.append(temp)
        return out
