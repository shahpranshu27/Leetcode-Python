class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        result=[]
        for index1 in range(9):
            for index2 in range(9):
                element=board[index1][index2]
                if element!=".":
                    result+=[(index1,element), (element,index2), (index1//3, index2//3, element)]
        return len(result) == len(set(result))
        # here, adding the elements in the form of tuples and then adding them in the list is done, to keep the track 
        # and ensure that there are no repeated elements in either rows or cols or sub-grids. if there will be any duplicates, 
        # we will get to know as the set removes all the duplicates, and the len(res) won't be = len(set(res))
