class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        start, end  = 0, len(matrix)-1
        

        while start<=end:
            mid = (start+end)//2
            row = matrix[mid]
            if target >= row[0] and target <= row[len(row)-1]:
                start = 0
                end = len(row)-1
                
                while start<=end:
                    mid = (start+end)//2
                    if row[mid] == target:
                        return True
                    elif row[mid] < target:
                        start = mid+1
                    else:
                        end = mid-1
                return False
            elif target < row[0]:
                end = mid-1
            else:
                start = mid+1
        
        return False
                 
