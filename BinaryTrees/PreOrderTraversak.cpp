// Link to Problem: https://leetcode.com/problems/binary-tree-preorder-traversal/
// Given the root of a binary tree, return the preorder traversal of its nodes' values.

// Example 1:

// Input: root = [1,null,2,3]
// Output: [1,2,3]

// Example 2:

// Input: root = []
// Output: []

// Example 3:

// Input: root = [1]
// Output: [1]

 void func(TreeNode* root, vector<int> &v){
     if(root==NULL)return;
     v.push_back(root->val);
     func(root->left,v);
     func(root->right,v);
     return;
 }
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> v;
        func(root,v);
        return v;
        
    }
};