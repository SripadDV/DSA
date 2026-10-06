class Solution:

    def checkMinPages(self, nums: list[int], mid: int):

        count = 1
        curSum = 0
        for num in nums:
            if curSum + num <= mid:
                curSum += num
            else:
                curSum = num
                count += 1
        
        return count


    def findPages(self, nums, m):
        if len(nums) < m:
            return -1
        
        low = max(nums)
        high = sum(nums)
        
        minPage = high

        while low<=high:
            mid = (low+high)//2
            count = self.checkMinPages(nums, mid)
            if  count > m:
                low = mid + 1
            else:
                ans = mid
                high = mid - 1
                 
        return ans