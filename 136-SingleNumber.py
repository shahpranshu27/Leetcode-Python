class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num # ^ is XOR, XOR os 0,0 and 1,1 is 0, and 0,1 and 1,0 is 1
            # So, here are the steps (remember, we need to convert these numbers 0, 4 and all in binary, then only we can do XORing) { Example: [4,1,2,1,2]}:
            # iteration 1: 0^4 = 4
            # iteration 2: 4^1 = 5
            # iteration 3: 5^1 = 7
            # iteration 4: 7^2 = 6
            # iteration 5: 6^2 = 4 (final answer)
        
        return result
