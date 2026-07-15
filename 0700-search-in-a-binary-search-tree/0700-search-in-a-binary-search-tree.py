# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def f(root):
            if not root:
                return None
            if root.val== val:
                return root
            if val<root.val:
                return f(root.left)
            else:
                return f(root.right)
        return f(root)
            

        