class Solution:
    def subarraySum(self, nums, k):
        hashStore = dict()
        hashStore[0] = 1
        curSum = 0
        count = 0
        for i in range(len(nums)):
            curSum += nums[i]
            if curSum - k in hashStore.keys():
                count += hashStore[curSum-k]
            hashStore[curSum] = hashStore.get(curSum, 0) + 1
        return count
      