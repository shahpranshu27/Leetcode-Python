class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = nums[0]+nums[1]+nums[2]
        nums.sort()
        
        if nums is None or len(nums)==0:
                return None

        for i in range(len(nums)-2):
            l,r = i+1, len(nums)-1

            while l<r:
                summ = nums[i]+nums[l]+nums[r]
                if summ == target:
                    return summ
                
                elif (abs(summ-target) < abs(ans-target)):
                    ans = summ
                
                elif summ<target:
                    l+=1
                else:
                    r-=1

        return ans
