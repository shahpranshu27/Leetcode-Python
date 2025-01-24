class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for index1 in range(len(nums)):
            for index2 in range(index1+1, len(nums)):
                if nums[index1]>nums[index2]:
                    nums[index1], nums[index2] = nums[index2], nums[index1]
