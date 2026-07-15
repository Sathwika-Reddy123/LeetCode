# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def f(root):
            if not root:
                return None
            if root == p or root == q:
                return root
            l=f(root.left)
            r=f(root.right)
            if l and r:
                return root
            return l if l else r
            
    
        return f(root)

             
        