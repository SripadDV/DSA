class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:        
        res = list()
        nums.sort()
        i = 0
        j = 0
        while i < len(nums)-3:
            j = i+1
            while j < len(nums)-2:
                l = j+1
                r = len(nums)-1
                while l<r:
                    if nums[i] + nums[j] + nums[l] + nums[r] == target:
                        res.append((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        while l<r and nums[l] == nums[l-1]:
                            l += 1
                    elif nums[i] + nums[j] + nums[l] + nums[r] < target:
                        l += 1
                    else:
                        r -= 1
                j += 1
                while j < len(nums)-2 and nums[j]==nums[j-1]:
                    j += 1
            i += 1
            while i < len(nums)-3 and nums[i]==nums[i-1]:
                i += 1
        
        return res
        
