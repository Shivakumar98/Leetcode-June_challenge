Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
    
        # Solution 2
        # we will calculate the Tree height both left and right 
        h_right,h_left=0,0
        L,R=root,root
        while L!=None:
            h_left+=1
            L=L.left 
        while R!=None:
            h_right+=1
            R=R.right 
        print(h_right,h_left)
        
        #if its a perfect Binary tree
        if h_right==h_left:
            val=int(math.pow(2,h_left)-1)
            print(val)
            return val
        return (self.countNodes(root.left)+self.countNodes(root.right)+1) 
        
        
        
        # Solution 1
        if root==None:
            return 0
        return (self.countNodes(root.left)+self.countNodes(root.right)+1)  # +1 is for root node
    
