class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        curMax = nums[0]
        count = 1

        for  i in range(1, len(nums)):
            if count == 0:
                curMax = nums[i]
                count = 1
            elif nums[i] == curMax:
                count += 1
            else:
                count -= 1
        return curMax
        