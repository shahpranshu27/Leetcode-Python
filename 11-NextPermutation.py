class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # i = len(nums)-2

        # while i>=0 and nums[i]>nums[i+1]:
        #     i-=1
        
        # if i>=0:
        #     j = len(nums)-1
        #     while j>i and nums[j]<=nums[i]:
        #         j-=1
            
        #     nums[i], nums[j] = nums[j], nums[i]
        
        # nums[i+1:] = reversed(nums[i+1:])

        n = len(nums)
        
        pivot = -1
        for index1 in range(len(nums)-2, -1, -1):
            if nums[index1]<nums[index1+1]:
                pivot=index1
                break
            
        
        if pivot!=-1:
            for index2 in range(len(nums)-1, pivot, -1):
                if nums[index2]>nums[pivot]:
                    nums[pivot], nums[index2] = nums[index2], nums[pivot]
                    break
                
        nums[pivot+1:] = reversed(nums[pivot+1:])
