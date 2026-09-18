class Solution:
    def longestSubarray(self, nums, k):
        hashStore = dict()
        hashStore[0] = 0
        maxSubArray = 0
        arraySum = 0

        for i in range(len(nums)):
            num = nums[i]
            arraySum += num
            key = arraySum - k 
            if key in hashStore.keys():
                maxSubArray = max(maxSubArray, i+1-hashStore[key])
            if arraySum not in hashStore.keys():
                hashStore[arraySum] = i+1
        
        return maxSubArray