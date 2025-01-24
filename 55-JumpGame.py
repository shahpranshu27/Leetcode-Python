class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxIndex=0
        for index in range(len(nums)):
            if index>maxIndex:
                return False
            
            maxIndex=max(maxIndex, index+nums[index])
        
        return True
