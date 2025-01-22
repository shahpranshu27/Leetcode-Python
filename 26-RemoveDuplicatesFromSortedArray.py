class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return None
        
        left = 0 # initialized to track position of last unique element

        for right in range(1, len(nums)):
            if nums[right]!=nums[left]:
                left+=1
                nums[left] = nums[right]
        
        return left+1
