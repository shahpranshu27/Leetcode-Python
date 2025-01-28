class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # maxProd=max(nums)
        # if len(nums)>1:
        #     for index1 in range(len(nums)-1):
        #         maxProd = max(maxProd, nums[index1+1]*nums[index1])
                
        #     return maxProd
        # return max(nums)
        
        res=max(nums)
        cur_max=cur_min=1

        for num in nums:
            temp=cur_max*num
            cur_max=max(temp, cur_min*num, num)
            cur_min=min(temp, cur_min*num, num)
            res=max(res, cur_max)
        
        return res

        
