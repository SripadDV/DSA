class Solution:
    def maxProduct(self, nums):
        curMin = nums[0]
        curMax = nums[0]
        totalMax = nums[0]
        tempMax = nums[0]
        for i in range(1, len(nums)):
            curMax = max(curMax*nums[i], max(curMin*nums[i], nums[i]))
            curMin = min(tempMax*nums[i], min(curMin*nums[i], nums[i]))
            totalMax = max(curMax, totalMax)
            tempMax = curMax
        return totalMax
        