class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # def markRow(i):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j]!=0:
        #             matrix[i][j]=-1

        # def markCol(j):
        #     for i in range(len(matrix)):
        #         if matrix[i][j]!=0:
        #             matrix[i][j]=-1

        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j]==0:
        #             markRow(i)
        #             markCol(j)

        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j]==-1:
        #             matrix[i][j]=0

        # rowLen = len(matrix)
        # colLen = len(matrix[0])

        n = len(matrix)
        m = len(matrix[0])
        
        # create an extra row and col, and firstly assign them 0s only. Then, if in matrix[i][j]==0, then mark row[i] and col[j]=1. Then iterate again, and if there's a 1, then mark whole row and col as 0

        row = [0]*n
        col = [0]*m

        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    row[i]=1
                    col[j]=1

        
        for i in range(n):
            for j in range(m):
                if row[i] or col[j]:
                    matrix[i][j]=0
