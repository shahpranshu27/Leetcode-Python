class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index=1
        occurance=1

        for index1 in range(1, len(nums)):
            if nums[index1]==nums[index1-1]:
                occurance+=1
            else:
                occurance=1
            
            if occurance<=2:
                nums[index]=nums[index1]
                index+=1
        
        return index
