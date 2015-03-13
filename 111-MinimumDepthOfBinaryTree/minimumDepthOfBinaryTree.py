# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys

class Solution:
    # @param root, a tree node
    # @return an integer
    #isNothing = 0
    count = 0
    
    def minDepth(self, root):
        if root == None:
            if not self.count:
                return 0
            else:
                #Important
                return sys.maxsize
        elif root.left == None and root.right == None:
            self.count += 1
            return 1
        else:
            self.count += 1
            return 1+min(self.minDepth(root.left), self.minDepth(root.right))
        