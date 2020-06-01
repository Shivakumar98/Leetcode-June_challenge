Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

Trivia:
This problem was inspired by this original tweet by Max Howell:

    Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            # print(root.val)
            root.left,root.right=root.right,root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        
        return root
        
        
        
        
        
        
        
        
        
        
#         a,b,c=[],[],[]
        
#         self.preorder(root,a)
#         self.inorder(root,b)
#         self.postorder(root,c)
#         print(a)
#         print(b)
#         print(c)
#     def preorder(self, root: TreeNode,a):
#         if root:
#             print(root.val)
#             root.left,root.right=root.right,root.left
#             self.preorder(root.left)
#             self.preorder(root.right)
            
#     def inorder(self, root: TreeNode,b):
#         if root:
            
#             self.preorder(root.left)
#             print(root.val)
#             b.append(root.val)
#             self.preorder(root.right)
#     def postorder(self, root: TreeNode,c):
#         if root:
            
#             self.preorder(root.left)
            
#             self.preorder(root.right)
#             print(root.val)
#             c.append(root.val)
        
