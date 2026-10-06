class Solution:
    def longestOnes(self, nums, k):
        #your code goes here
        left = 0
        right = 0

        curOne = 0
        maxOne = 0
        curk = 0
        while right < len(nums):
            if nums[right] == 1:
                curOne += 1
                maxOne = max(maxOne, curOne)    
            else:
                if k == 0:
                    curOne = 0
                elif curk < k:
                    curOne += 1
                    curk += 1
                    maxOne = max(maxOne, curOne)
                else:
                    while left < right:
                        if nums[left] == 1:
                            left += 1
                        else:
                            left += 1
                            break
                    
                    curOne = right - left + 1
                    maxOne = max(maxOne, curOne)
            right += 1
        return maxOne

                            