class Solution:

    def rootHelper(self, m: int, n: int, mid: int):
        x = mid
        product = 1
        while n>0:
            if (n&1)!=0:
                product *= x
                if product > m:
                    return 2
            x *= x
            n >>= 1
        if product == m:
            return 1
        return 0

    def NthRoot(self, n, m):
        if m == 1:
            return 1
        if n == 1:
            return m

        left = 1
        right = m
        
        while left<=right:
            mid = (left+right)//2
            ans = self.rootHelper(m, n, mid)
            if ans == 1:
                return mid
            elif ans == 0:
                left = mid+1
            else:
                right = mid-1
        
        return -1

      