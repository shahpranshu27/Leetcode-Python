class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range(len(numbers)):
        #     for j in range(i+1, len(numbers)):
        #         if numbers[i]+numbers[j]==target:
        #             return [i+1, j+1]

        # length=len(numbers)
        left=0
        right=len(numbers)-1

        while left<right:
            currentSum=numbers[left]+numbers[right]
            if currentSum==target:
                return [left+1, right+1]
            
            elif currentSum<target:
                left+=1
            
            else:
                right-=1
        return []
