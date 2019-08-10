#problem link:https://leetcode.com/problems/range-sum-of-bst/submissions/
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        range_sum = 0
        stack = [root]
        while stack:
            cur_node = stack.pop()
            if cur_node:
                if L <= cur_node.val <= R:
                    range_sum += cur_node.val
                if L < cur_node.val:
                    stack.append(cur_node.left)
                if cur_node.val < R:
                    stack.append(cur_node.right)
        return range_sum