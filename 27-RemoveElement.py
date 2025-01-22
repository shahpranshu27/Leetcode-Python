class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j=0

        for item in range(len(nums)):
            if nums[item] != val:
                nums[j] = nums[item]
                j+=1
            
        return j
