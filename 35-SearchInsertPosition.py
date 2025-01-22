class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for index in range(len(nums)):
            if nums[index] == target:
                return index

            elif target<nums[index]:
                return index
            
        return len(nums)
            
