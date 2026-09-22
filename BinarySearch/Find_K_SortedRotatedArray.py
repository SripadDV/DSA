class Solution:

    def binarySearch(self, nums: list[int], left: int, right: int, k: int) -> int:
        if left==right:
            if nums[left] == k:
                return left
            return -1
        if left>right:
            return -1
        mid = (left+right)//2
        if nums[mid] == k:
            return mid
        if nums[mid]<k:
            return self.binarySearch(nums, mid+1, right, k)
        return self.binarySearch(nums, left, mid, k)
    
    def checkRotationBinarySearch(self, nums: list[int], left: int, right: int, k: int) -> int:
        if left == right-1:
            if nums[left] == k: 
                return left
            if nums[right] == k:
                return right
            return -1
        mid = (left+right)//2
        if nums[left] <= nums[mid]:
            if nums[left] <= k and k <= nums[mid]:
                return self.binarySearch(nums, left, mid, k)
            return self.checkRotationBinarySearch(nums, mid, right, k)
        else:
            if nums[mid] <= k and k <= nums[right]:
                return self.binarySearch(nums, mid, right, k)
            return self.checkRotationBinarySearch(nums, left, mid, k)

    def search(self, nums: list[int], target: int) -> int:
        k = target
        if len(nums) == 1:
            if nums[0] == k:
                return 0
            return -1

        if nums[0] < nums[len(nums)-1]:
            return self.binarySearch(nums, 0, len(nums)-1, k)

        return self.checkRotationBinarySearch(nums, 0, len(nums)-1, k)
        