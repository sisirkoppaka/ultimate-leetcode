# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        
        if not p or not q:
            if not p and not q:
                return True
            else:
                return False
        elif p.val != q.val:
            return False
        #elif p.val == q.val and p.right == None and p.right == q.right:
        #    return True
        #else:
        #    return False

        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)