class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        
        self.flatten(root.left)
        self.flatten(root.right)
        
        left = root.left
        right = root.right
        root.left = None
        root.right = left
        
        temp = root
        while not temp or temp.right:
            temp = temp.right
        temp.right = right