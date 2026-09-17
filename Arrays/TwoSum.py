class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashStore = dict()
        for i in range(len(nums)):
            if target-nums[i] in hashStore.keys():
                return [hashStore[target-nums[i]], i]
            hashStore[nums[i]] = i
