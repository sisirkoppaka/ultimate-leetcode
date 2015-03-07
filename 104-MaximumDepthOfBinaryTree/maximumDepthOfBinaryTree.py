# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        try:
            if not root:
                return 0
            return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
        except:
            return 1
        #if self.left != None:
        #   return (1 + maxDepth(self.left))
        #if self.right != None:
        #    maxDepth(self.right)
        #if self.left == None and self.right == None:
            #Leaf node
         #   return 1+
        
        