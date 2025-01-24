class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq_count = {}

        for num in nums:
            if num in freq_count:
                freq_count[num]+=1
            
            else:
                freq_count[num] = 1

        for key, val in freq_count.items():
            if val==1:
                return key
