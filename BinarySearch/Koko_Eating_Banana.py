class Solution:
    def minimumRateToEatBananas(self, nums, h):
        if len(nums) == 1:
            return math.ceil(nums[0]/h)

        low = 1
        high = nums[0]
        for num in nums:
            high = max(num, high)
        
        minBananana = high
        
        while low <= high:
            mid = (low+high)//2
            
            totalHours = 0
            for num in nums:
                totalHours += math.ceil(num/mid)
            
            if totalHours <= h:
                minBananana = min(minBananana, mid)
                high = mid-1
            else:
                low = mid+1
        
        return minBananana