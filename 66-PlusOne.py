class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        for index in range(n-1, -1, -1):
            if digits[index]<9:
                digits[index]+=1
                return digits
            
            digits[index]=0
        
        return [1]+digits
