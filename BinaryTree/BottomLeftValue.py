'''513. Find Bottom Left Tree Value
Given the root of a binary tree, return the leftmost value in the last row of the tree.

Example 1:
Input: root = [2,1,3]
Output: 1

Example 2:
Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if(not node):
                return 0, 0
              
            if(not node.left and not node.right):
                # leaf node
                return 1, node.val
            
            l_depth, l_val = dfs(node.left)
            r_depth, r_val = dfs(node.right)

            val = l_val
            if(r_depth > l_depth):
                val = r_val

            # return current depth and its leftmost value
            return (max(l_depth, r_depth)+1, val)
        
        d, value = dfs(root)
        return value
        
