# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max_path_dict = {}
        self.res = float('-inf') 
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
            
        self.dfs(root)
        print(self.max_path_dict)
        return self.res
    def dfs(self, root: Optional[TreeNode]) -> int:
        # correct
        if root is None:
            return 0
        
        

        # max_path for node
        left_max_path = self.dfs(root.left)
        right_max_path = self.dfs(root.right)

        local_max = max(
            self.res,
            root.val,                 # take neither branch
            root.val + left_max_path,
            root.val + right_max_path,         # take only right
            root.val + left_max_path + right_max_path,  # take both
        )
        # update global max
        self.res = max(self.res, local_max)

        return max(root.val, root.val + left_max_path, root.val + right_max_path)

        


        