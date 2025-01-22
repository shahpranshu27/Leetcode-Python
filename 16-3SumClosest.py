class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = nums[0]+nums[1]+nums[2]
        nums.sort()
        
        if nums is None or len(nums)==0:
                return None

        for index1 in range(len(nums)-2):
            left, right = index1+1, len(nums)-1

            while left<right:
                summ = nums[index1]+nums[left]+nums[right]
                if summ == target:
                    return summ
                
                elif (abs(summ-target) < abs(ans-target)):
                    ans = summ
                
                elif summ<target:
                    left+=1
                else:
                    right-=1

        return ans
