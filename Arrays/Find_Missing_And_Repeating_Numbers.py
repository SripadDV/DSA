class Solution:
    def findMissingRepeatingNumbers(self, nums):

        xor = 0
        for i in range(len(nums)):
            xor ^= nums[i]
        
        for i in range(1, n+1):
            xor ^= i
        
        number =  (xor ^ ( xor-1)) & xor #get the right most set bit

        zero = 0
        one = 0

        for i in nums:
            if number & i != 0:
                one ^= i
            else:
                zero ^= i
        
        for i in range(1, n+1):
            if number & i != 0:
                one ^= i
            else:
                zero ^= i
        
        count = 0
        for i in nums:
            if i == zero:
                count += 1
        
        if count == 2:
            return [zero, one]
        else:
            return [one, zero]
