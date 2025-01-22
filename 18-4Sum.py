class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if nums is None or len(nums)<4:
            return []

        result=[]
        
        nums.sort()

        for index1 in range(len(nums)-3):
            if index1>0 and nums[index1] == nums[index1-1]:
                continue
            
            for index2 in range(index1+1, len(nums)-2):
                if index2>index1+1 and nums[index2] == nums[index2-1]:
                    continue
                
                left = index2+1
                right = len(nums)-1
                
                while left<right:
                    four_sum=nums[index1]+nums[index2]+nums[left]+nums[right]
                    if four_sum==target:
                        result.append([nums[index1], nums[index2], nums[left], nums[right]])
                        left+=1
                        right-=1
                    
                        while left<right and nums[left]==nums[left-1]:
                            left+=1
                        
                        while left<right and nums[right]==nums[right+1]:
                            right-=1
                    elif four_sum < target:
                        left+=1
                    
                    else:
                        right-=1
                    
        return result
