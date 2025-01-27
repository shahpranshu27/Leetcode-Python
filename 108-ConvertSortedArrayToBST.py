# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
        '''
        TreeNode acts as a "container" for the values at each level in the recursion.
The sortedArrayToBST function keeps splitting the array at its middle, choosing the middle element as the node, and recursively building the left and right subtrees.
Dividing the array into left and right parts ensures the tree remains balanced because each division is essentially halving the array, leading to a balanced structure.
This continues until there are no more elements to process, and the recursion terminates.
        '''
