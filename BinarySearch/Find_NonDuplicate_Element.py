class Solution:

    def checkSingleElement(self, nums: list[int], left: int, right: int) -> int:
        print(left, " ", right)
        if left == right:
            return nums[left]
        mid = (left+right)//2

        if left == right-1:
            if left == 0:
                return nums[left]
            elif right == len(nums)-1:
                return nums[len(nums)-1]
            elif (nums[mid] != nums[mid-1]) and (nums[mid] != nums[mid+1]):
                return nums[mid]
            else: #nums[mid] != nums[mid+1] and nums[mid+1] != nums[mid+2]:
                return nums[mid+1]
        else:
            if mid%2==0:
                if nums[mid] == nums[mid+1]:
                    return self.checkSingleElement(nums, mid+1, right)
                else:
                    return self.checkSingleElement(nums, left, mid)
            else:
                if nums[mid] == nums[mid-1]:
                    return self.checkSingleElement(nums, mid+1, right)
                else:
                    return self.checkSingleElement(nums, left, mid)

    def singleNonDuplicate(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        return self.checkSingleElement(nums, 0, len(nums)-1)
       