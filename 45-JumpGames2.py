class Solution:
    def jump(self, nums: List[int]) -> int:
        # reach -> max reachable index
        # last  -> rightmost index reached
        # count -> number of jumps
        reach, last, count=0,0,0

        for index in range(len(nums)-1):
            reach=max(reach, index+nums[index])

            # checks if i has reached the last index that can be reached with the current number of jumps
            # have we reached the last position that we could have reached till now?
            if i==last:
                # update last to new reachable index
                last=reach
                count+=1
        
        return count
