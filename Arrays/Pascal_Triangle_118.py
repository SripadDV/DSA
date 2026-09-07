class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = list()
        row = list()
        row.append(1)
        res.append(row)
        
        for i in range(1,numRows):
            row = res[-1]
            arr = list()
            arr.append(1)
            for j in range(len(row)-1):
                arr.append(row[j]+row[j+1])
            arr.append(1)
            # print(arr)
            res.append(arr)
        
        return res

soln = Solution()
print(soln.generate(5))