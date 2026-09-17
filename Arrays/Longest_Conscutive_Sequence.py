class Solution:
    def longestConsecutive(self, nums):
        numSet = set(nums)
        maxCount = 0
        count = 0
        for num in nums:
            if num-1 in numSet:
                continue
            count = 0
            numSeq = num
            while numSeq in numSet:
                count += 1
                numSeq += 1
            maxCount = max(count, maxCount)

        return maxCount