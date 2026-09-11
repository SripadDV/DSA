class Solution:
    
    def mirror(self, nums: List[int], i: int) -> List[int]:
        j = 0
        for i in range(i, i+(len(nums)-i)//2):
            temp = nums[i]
            nums[i] = nums[len(nums)-1-j]
            nums[len(nums)-1-j] = temp
            j += 1
        return nums


    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=1:
            return
        asc = True
        for i in reversed(range(len(nums)-1)):
            if nums[i] >= nums[i+1]:
                continue
            else:
                asc = False
                for j in reversed(range(len(nums))):
                    if nums[j] > nums[i]:
                        temp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = temp
                        print(nums)
                        self.mirror(nums, i+1)
                        break
            break
        if asc:
            self.mirror(nums, 0)
        
        