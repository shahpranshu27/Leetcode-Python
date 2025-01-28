class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for index in nums:
            if index==0:
                nums.remove(index)
                nums.append(index)
            
        return nums
