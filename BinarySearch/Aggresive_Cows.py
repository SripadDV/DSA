class Solution:

    def checkCanPlaceCows(self, nums, k , d) -> bool:
        count = 1
        lastPlace = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - lastPlace>=d:
                count += 1
                if count == k:
                    return True
                lastPlace = nums[i]
        return False

    def aggressiveCows(self, nums, k):
        nums.sort()

        low = 1
        high = nums[len(nums)-1] - nums[0]
        maxDistance = 0
        while low <= high:
            mid = (low+high)//2
            ans = self.checkCanPlaceCows(nums, k, mid)
            if ans:
                maxDistance = max(maxDistance, mid)
                low = mid + 1
            else:
                high = mid - 1
        return maxDistance

