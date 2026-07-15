# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def f(root):
            if not root:
                return TreeNode(val)
            if root.val < val:
                root.right=f(root.right)
            else:
                root.left=f(root.left)
            return root
        return f(root)
        
            
        