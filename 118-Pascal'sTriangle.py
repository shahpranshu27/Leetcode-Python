class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[[1]]

        for i in range(numRows-1):
            # here, I am taking 0 before and after the array, just to take the sum of 0+1 and result in 1, in that way i can take sum of 2 consecutive nos. from prev rows and store that in that particular row. res[-1] is prev row, and adding 0 before and after that row, and storing that in temp array
            temp = [0] + res[-1] + [0]
            row=[]
            for j in range(len(res[-1])+1):
                row.append(temp[j]+temp[j+1]) # adding 2 consecutive nos., and storing that in row
            res.append(row)
        return res
