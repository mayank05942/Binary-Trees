Prob: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
___________________________________________________________________________________________________________________________________
https://www.youtube.com/watch?v=YMVn56IQhZo      -thecodingworld
https://www.youtube.com/watch?v=yqAab6aaVs8     - Codebix
https://www.youtube.com/watch?v=W9irlUOf6lI      - coding ninjas



Explanation: Pre: node,left,right 
             In : left,node,right

Algo: first val of preorder array is always root node and if we find that value in Inorder array we can get left and right half elements

first find root idx in inorder -> slice inorder to inorder_left and  inorder_right
similary slice preorder -> preorder_left and right
Now make recursive calls for left and right elements

Base Case: When inorder contains only 1 element then return  that element as a Treenode
           When inorder contains no element then return None
___________________________________________________________________________________________________________________________________

Code:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(preorder[0])
        
        node = TreeNode(preorder[0])
        
        curr_root_idx = inorder.index(preorder[0])
        
        inorder_left = inorder[:curr_root_idx]
        inorder_right = inorder[curr_root_idx+1:]
        preorder_left = preorder[1:curr_root_idx+1]
        preorder_right = preorder[curr_root_idx+1:]
        
        node.left = self.buildTree(preorder_left,inorder_left)
        node.right = self.buildTree(preorder_right,inorder_right)
        
        return node
       
