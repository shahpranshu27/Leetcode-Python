class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums is None or len(nums) == 0:
            return None
        
        set1 = set()
        nums.sort()

        for index1 in range(len(nums)-2): 
        # len(nums)-2 -> if we are at 2nd last element, then we wouldn't have sufficient elements to add 3 elements and sum up to 0
            if index1!=0 and nums[index1] == nums[index1-1]:
                continue
            
            left,right = index1+1, len(nums)-1 # for every nums[index1] element, we check from leftmost and rightmost elements and do the sum to see if sum adds up to 0

            while left<right:
                if nums[index1] + nums[left] + nums[right] == 0:
                    set1.add((nums[index1], nums[left], nums[right]))
                    left+=1
                    right-=1 # move the l and r pointers right and left respectively
                
                elif nums[index1]+nums[left]+nums[right]>=0:
                    right-=1 # as array is sorted from ascending to descending, if the sum>0, we need to decrease sum thus we move leftwards, and vice versa for sum<0
                
                else:
                    left+=1

        return list(set1)
