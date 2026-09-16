class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = list()
        for i in range(n):
            row.append(1)
        
        for i in range(1, m):
            for j in range(1, n):
                row[j] = row[j]+row[j-1]
        return row[-1]