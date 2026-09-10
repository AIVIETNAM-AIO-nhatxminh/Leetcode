# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        result = 0

        def countTree(self, root: TreeNode) -> tuple[int, int]:
            nonlocal result
            left = 0
            right = 0
            left_length = 0
            right_length = 0
            if self.left: 
                left, left_length = self.countTree(self.left)
            if self.right: 
                right, right_length = self.countTree(self.right)

            length = left_length + right_length + 1
            total = root.val + left + right

            if total // length == root.value:
                result += 1 
            return total, length

        countTree(self, root) 
        return result
